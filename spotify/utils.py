from .models import SpotifyToken
from django.utils import timezone
from datetime import timedelta
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from requests import post,get

BASE_URL = 'https://api.spotify.com/v1/me/'

#flow:
#1.authorize user and get AUTHORIZATION CODE
#2. use AUTHORIZATION CODE to obtain ACCESS TOKEN & REFRESH TOKEN
#3. use REFRESH TOKEN to obtaine new ACCESS TOKEN every 1 hour

# get user tokens based on session id
def get_user_tokens(session_id):

    user_tokens=SpotifyToken.objects.filter(user=session_id)

    if user_tokens.exists():

        return user_tokens[0]

    else:
        return None

#update or create a token
def update_or_create_user_tokens(session_id,access_token,token_type,expires_in,refresh_token):

    #get token

    tokens = get_user_tokens(session_id)

    #set expiry time (time at the moment + duration left before expiring)

    expires_in = timezone.now() + timedelta(seconds=expires_in)

    #if token is already available, refresh them

    if tokens:

        tokens.access_token = access_token
        tokens.token_type = token_type
        tokens.expires_in = expires_in
        tokens.refresh_token = refresh_token
        tokens.save(update_fields=['access_token','token_type','expires_in','refresh_token'])

    #if it's new, create one
    else:

        tokens = SpotifyToken(user=session_id,access_token=access_token,token_type=token_type,expires_in=expires_in,refresh_token=refresh_token)

        tokens.save()


#check if user is autheticated

def is_spotify_authenticated(session_id):

    tokens = get_user_tokens(session_id)

    #if exists
    if tokens:

        expiry = tokens.expires_in

        #check if it has already expired or not

        if expiry <= timezone.now():

            refresh_spotify_token(session_id)

        return True

    #if not exist

    return False


#check expiration and refresh

def refresh_spotify_token(session_id):

    #get refresh token from the token record

    refresh_token = get_user_tokens(session_id).refresh_token

    #post refresh code
    
    response = post('https://accounts.spotify.com/api/token', data={


                    
        'grant_type':'refresh_token',                                                     
        'refresh_token':refresh_token,                            
                                           
        'client_id':CLIENT_ID,
                                                     
        'client_secret':CLIENT_SECRET,


                                                       
        }).json()

    print(response)
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    #refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')

    #update tokens
    update_or_create_user_tokens(session_id,access_token,token_type,expires_in,refresh_token)

def execute_spotify_api_request(session_id,endpoint,post_=False,put_=False):

    tokens = get_user_tokens(session_id)

    headers={'Content-Type':'application/json',
            'Authorization':'Bearer '+tokens.access_token}

    #if action is post

    if post_:

        post(BASE_URL + endpoint, headers=headers)
        print('done')

    if put_:

        put(BASE_URL + endpoint, headers=headers)

    response = get(BASE_URL + endpoint, {}, headers=headers) 


    try: 

        return response.json() 

    except: 

        return {'Error': 'Issue with request'}







