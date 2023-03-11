from django.db import models
from django.contrib.auth.models import User
# main_app models


class Room(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=100, null=True)


class Chat(models.Model):
    message = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
