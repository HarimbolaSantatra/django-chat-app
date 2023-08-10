# Chat Application

## About 
This is a chat application made with Django.

## Installation
This application requires the following dependencies:
- Django
- Channels & Daphne
- PostgreSQL database
- redis server

Clone this repository:

	git clone https://github.com/HarimbolaSantatra/django_chat_app.git
	cd django_chat_app

Install all the Python's dependencies:

	python -m pip install -r requirements.txt

Activate redis and mysql server:

	sudo systemctl start redis-server postgresql

Create the postgresql database:

	$ psql -U <username> -d django_chat
	#CREATE DATABASE django_chat;

Use the _psql-dump.sql_ file to upload the table inside the database.

	psql django_chat < psql-dump.sql

Alternatively, if you want a clean database, you can skip the last step and let migration create the database for you. 

__Do not forget to correctly set up your _setting.py_ database settings.__

### User
The login system uses traditional Django authentication. TO add user, add Django superuser.

	python manage.py createsuperuser

## Branch
- master
- stable: use MySQL and no Vercel config files

## Resources
- [Django Documentation][1]
- A chat tutorial:  https://www.honeybadger.io/blog/django-channels-websockets-chat/

### WebSocket
WebSocket maintain a communication between session during a whole session, contrary to HTTP Request where one actor wait for a request before sending a response.
- [WebSocket API][5]

### Channels tutorial
- [Channels documentation][2]
- [Quick introduction][3]: Channels Documentation
- [Consumer][4]

## Feedback and Issues
Feel free to raise issues or to provide any feeback.

And again, Thanks for visiting !

[1]: docs.djangoproject.com
[2]: https://channels.readthedocs.io/en/stable/tutorial/index.html
[3]: https://channels.readthedocs.io/en/stable/introduction.html
[4]: https://channels.readthedocs.io/en/stable/topics/consumers.html 
[5]: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications 
