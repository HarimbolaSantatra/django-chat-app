from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # For login required decorator
from django.contrib.auth.models import User
from main_app.models import Room, Chat

import json

@login_required(login_url='login')
def index(request):
    rooms = Room.objects.all()
    context = {
        'username': request.session['username'],
        'rooms': rooms
    }
    return render(request, "index.html", context=context)


@login_required(login_url='login')
def room(request, room_name):
    username = request.session['username']
    current_room = Room.objects.get(name=room_name)
    chats = Chat.objects.filter(room=current_room)
    paginated_chats = Chat.get_samples(chats, 5)

    context = {
        'username': username,
        'room_name': room_name,
        'chat_per_day': Chat.sort_chats_per_day_per_hour(paginated_chats[-1], username),
    }
    return render(request, "room.html", context)
