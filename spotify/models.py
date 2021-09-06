from django.db import models
from api.models import Room

# Create your models here.
class SpotifyToken(models.Model):

    user = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)

# saves every vote by every user on a single song that is playing currently

class Vote(models.Model):

    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    song_id = models.CharField(max_length=50)

