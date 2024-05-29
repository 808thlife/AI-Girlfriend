from django.urls import path

from . import consumers

ws_urlpatterns = [
    path("ws/chat/<str:hash>", consumers.ChatConsumer.as_asgi())
]