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
    chat_messages = []
    for chat in chats:
        isOwner = (chat.user.username == username)
        class_name = "primary-message-row" if isOwner else "secondary-message-row"
        new_chat = { 
            "username":chat.user.username, 
            "message":chat.message,
            "class_name": class_name
            }
        chat_messages.append(new_chat)
    context = {
        'username': username,
        'room_name': room_name,
        'chat_message': chat_messages
    }
    return render(request, "room.html", context)
