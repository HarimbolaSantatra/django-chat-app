from django.shortcuts import render
from django.http import JsonResponse
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
def load_messages(request, room_name):
    """
    Return a json response, containing the next message.
    """

    username = request.session['username']
    current_room = Room.objects.get(name=room_name)

    # Query a number of chat message. Invert sort by date
    chats = Chat.objects.filter(room=current_room).order_by('-date')[:10]

    # update message index
    request.session['next_message_index'] += 1

    response = {
        'username': username,
        'room_name': room_name,
        'chat_per_day': Chat.sort_chats_per_day_per_hour(chats, username),
    }

    return JsonResponse(response)


@login_required(login_url='login')
def room(request, room_name):

    request.session['next_message_index'] = 0

    context = json.loads(load_messages(request, room_name).content)

    return render(request, "room.html", context)

