from django.urls import path
from . import views

urlpatterns = [

        #as_view() is necessary, otherwise 2 arguments are given 
        path('RoomView',views.RoomView.as_view()),

        path('CreateRoomView',views.CreateRoomView.as_view()),

        path('GetRoomView',views.GetRoomView.as_view()),

        path('JoinRoomView',views.JoinRoomView.as_view()),

        path('UserInRoom',views.UserInRoom.as_view()),

        path('UserLeaveRoom',views.UserLeaveRoom.as_view()),

        path('UpdateRoomView',views.UpdateRoomView.as_view()),

            ]
