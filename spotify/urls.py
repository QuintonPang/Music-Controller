from django.urls import path
from .views import *

urlpatterns=[


        path('GetAuthUrl',Auth.as_view()),
        path('Redirect',spotify_callback),
        path('IsAuthenticated',IsAuthenticated.as_view()),
        path('CurrentSong',CurrentSong.as_view()),


        ]
