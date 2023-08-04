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
    def sort_chats_per_day(chats, current_username):
        chat_per_day = []
        current_day = None
        for chat in chats:
            isOwner = (chat.user.username == current_username)
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

        return chat_per_day