from django.urls import path
from .views import *

urlpatterns=[


        path('GetAuthUrl',Auth.as_view()),
        path('Redirect',spotify_callback),
        path('IsAuthenticated',IsAuthenticated.as_view()),
        path('CurrentSong',CurrentSong.as_view()),
        path('PlaySong',PlaySong.as_view()),
        path('PauseSong',PauseSong.as_view()),
        path('SkipSong',SkipSong.as_view()),


        ]
