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
    Take a request and return a json response containing the next message.
    """

    MESSAGE_PER_PAGE = 4

    # try:
    #     ci = request.session['current_index']
    # except KeyError:
    #     request.session['current_index'] = 0
    #     ci = 0

    ci = request.session['current_index']

    username = request.session['username']
    current_room = Room.objects.get(name=room_name)

    # Query a number of chat message. Invert sort by date
    # We extract the chat object in reverse order so notice how we index the result
    # due to UI implementation, we must reverse the order of the result
    chats = Chat.objects.filter(room=current_room).order_by('-date')[ci:MESSAGE_PER_PAGE+ci]

    # # update message index
    request.session['current_index'] = ci + MESSAGE_PER_PAGE

    response = {
        'username': username,
        'room_name': room_name,
        'chat_per_day': Chat.sort_chats_per_day_per_hour(chats, username),
        'ci': ci,
        'session_index': request.session['current_index'],
    }

    return JsonResponse(response)


@login_required(login_url='login')
def room(request, room_name):

    # We extract the chat object in reverse order so the 
    # current index is the last and it goes backwards until it reach 0
    current_room = Room.objects.get(name=room_name)

    context = json.loads(load_messages(request, room_name).content)

    request.session['current_index'] = 0

    return render(request, "room.html", context)

