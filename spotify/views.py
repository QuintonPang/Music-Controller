from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from .models import SpotifyToken
from requests import Request,post
from rest_framework import status
from .utils import *
from api.models import Room

# Create your views here.

#get url for authentication
class Auth(APIView):

    def get(self, request, format=None):

        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

        url = Request('GET','https://accounts.spotify.com/authorize',params={


                    'scope':scopes,
                    'response_type':'code',
                    'redirect_uri':REDIRECT_URI,
                    'client_id':CLIENT_ID,

            }).prepare().url

        return Response({'url':url},status=status.HTTP_200_OK)

def spotify_callback(request,format=None):

    code = request.GET.get('code')
    error = request.GET.get('error')

    #post authorization and get response(token)

    response = post('https://accounts.spotify.com/api/token', data={


            'grant_type':'authorization_code',
            'code':code,
            'redirect_uri':REDIRECT_URI,
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET,


            }).json()

    print(response)

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    refresh_token = response.get('refresh_token')

    if not request.session.exists(request.session.session_key):

        request.session.create()


    update_or_create_user_tokens(request.session.session_key,access_token,token_type,expires_in,refresh_token)

    #redirect to frontend app, anything after colon means the name of view

    return redirect('frontend:')

#check if is authenticated using session key
class IsAuthenticated(APIView):

    def get(self,request,format=None):


        is_authenticated = is_spotify_authenticated(self.request.session.session_key)

        return Response({'status':is_authenticated},status=status.HTTP_200_OK)


   
class CurrentSong(APIView):

    def get(self,request,format=None):

        room_code = self.request.session.get('roomCode')

        room = Room.objects.filter(code = room_code)

        if room.exists():

            room=room[0]

        else:
            return Response({}, status = status.HTTP_404_NOT_FOUND)

        host = room.host

        endpoint = 'player/currently-playing'

        response = execute_spotify_api_request(host,endpoint)

        if 'error' in response or 'item' not in response:

            return Response({},status=status.HTTP_204_NO_CONTENT)

        item = response.get('item')
        progress = response.get('progress_ms')
        image = item.get('album').get('images')[0].get('url')
        duration = item.get('duration_ms')
        is_playing = response.get('is_playing')
        song_id = item.get('id')
        song_name = item.get('album').get('name')

        artists = ""

        for i,artist in enumerate(item.get('album').get('artists')):

                if i>0:

                    artists+=","

                artists+=artist.get('name')

        song = {

            'progress':progress,
            'image' : image,
            'duration' : duration,
            'is_playing' : is_playing,
            'song_id': song_id,
            'artists':artists,
            'song_name' : song_name,


            }

        


        return Response(song,status=status.HTTP_200_OK)


