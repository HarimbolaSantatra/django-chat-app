# Generated by Django 4.1.7 on 2023-08-03 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0006_chat_message_room_description_room_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]