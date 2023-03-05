from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # Take a route (in regex format here) and route it to the consumer ChatConsumer
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
