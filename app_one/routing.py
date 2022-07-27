from django.urls import  include, path, include
from app_one import consumers
urlpatterns = [
    path('ws/global', consumers.Mysync.as_asgi() ),
    path('ws/<str:roomname>/' , consumers.Myprivateroom.as_asgi() ),
    path('ws/chatbot' , consumers.Bot_reply.as_asgi())
]
#websocket url
