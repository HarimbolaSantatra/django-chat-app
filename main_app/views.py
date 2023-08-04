from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # For login required decorator
from django.contrib.auth.models import User
from main_app.models import Room, Chat

import json
from datetime import datetime

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
    chat_per_day = []
    current_day = None
    for chat in chats:
        isOwner = (chat.user.username == username)
        class_name = "primary-message-row" if isOwner else "secondary-message-row"
        new_chat = { 
            "username":chat.user.username, 
            "message":chat.message,
            "time":chat.get_time(),
            "class_name": class_name
            }

        # Sort chat messages per day
        if current_day == None or current_day != chat.get_day():
            current_day = chat.get_day()
            chat_per_day.append({"day": current_day, "chats": [new_chat]})
        else:
            chat_per_day[-1]["chats"].append(new_chat)

    test_var = chat_per_day[-1]
    context = {
        'username': username,
        'room_name': room_name,
        'chat_per_day': chat_per_day,
        "test_var": test_var
    }
    return render(request, "room.html", context)
