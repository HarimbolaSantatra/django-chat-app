from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("load/<str:room_name>/", views.load_messages, name="load_messages"),
]
