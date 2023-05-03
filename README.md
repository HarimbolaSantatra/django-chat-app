# Chat Application
## About 
This is a chat application made with Django.

## Installation
This application requires the following dependencies:
- Django
- Channels & Daphne
- MySQL database

Clone this repository:

	git clone https://github.com/HarimbolaSantatra/django_chat_app.git
	cd django_chat_app

Install all the Python's dependencies:

	python -m pip install -r requirements.txt

Use the dump.sql_ file to upload the MySQL table inside your MySQL database.

	mysql -u <username> -p < dump.sql

Alternatively, if you want a clean database, you can skip this step and let migration create the database for you, provided that you correctly set up your _setting.py_ database backend.

Use the username/password: root/root to login to the application and to Django admin page. Feel free to add users.

## WebSocket
WebSocket maintain a communication between session during a whole session, contrary to HTTP Request where one actor wait for a request before sending a response.

## Resources
- [Django Documentation][1]
- A chat tutorial:  https://www.honeybadger.io/blog/django-channels-websockets-chat/

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