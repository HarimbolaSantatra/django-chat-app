from django.contrib import admin
from .models import Room, Chat

# Make a customized admin interface
@admin.register(Chat)
class ChatInterfaceAdmin(admin.ModelAdmin):
	list_display = ('message', 'user', 'room')

@admin.register(Room)
class RoomInterfaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
