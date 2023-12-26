from django.urls import re_path
from chat import consumers

websocket_patterns = [
    re_path(r'ws/socket-server/',consumers.ChatConsumer.as_asgi())
]