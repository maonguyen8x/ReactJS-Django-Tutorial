from django.urls import path
from .views import CreateRoom, GetRoom, JoinRoom, LeaveRoom, RoomView, UpdateRoom, UserInRoom

urlpatterns = [
    path('create-room', CreateRoom.as_view()),
    path('room', RoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view())
]