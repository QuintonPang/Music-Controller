from django.urls import path
from . import views

# for spotify redirect to recognize
app_name = "frontend"

urlpatterns=[


        path('',views.App,name=""),
        path('CreateRoom',views.App),
        path('GetRoom/<str:code>',views.App),
        path('JoinRoom',views.App),  
        
        ]
