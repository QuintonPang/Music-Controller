from django.urls import path
from . import views

urlpatterns=[


        path('',views.App),
        path('CreateRoom',views.App),
        path('GetRoom/<str:code>',views.App),
        path('JoinRoom',views.App),  
        
        ]
