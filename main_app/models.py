from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=100, null=True)


class Chat(models.Model):
    message = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def get_day(self):
        return self.date.strftime("%b %d")

    def get_time(self):
        return self.date.strftime("%I:%M %p")


    @staticmethod
    def sort_chats_per_day_per_hour(chats, current_username):
        chat_per_day = []
        current_day = None
        current_hour = None
        for chat in chats:
            isOwner = (chat.user.username == current_username)
            class_name = "primary-message-row" if isOwner else "secondary-message-row"

            # style_username: show username only if message owner is not current logged user
            style_username = chat.user.username if not isOwner else ""

            new_chat = { 
                "username":style_username, 
                "message":chat.message,
                "time":chat.get_time(),
                "class_name": class_name
                }

            # Sort chat messages per day
            if current_day == None or current_day != chat.get_day():
                current_day = chat.get_day()
                chat_per_day.append({"day": current_day, "per_hour": []})

            # Sort messages per hour
            if current_hour == None or current_hour != chat.get_time():
                current_hour = chat.get_time()
                chat_per_day[-1]['per_hour'].append({"hour": current_hour, "chats": [new_chat]})
            else:
                chat_per_day[-1]['per_hour'][-1]["chats"].append(new_chat)


        return chat_per_day