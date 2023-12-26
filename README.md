Realtime Communication.

Using Django Channels and WebSockets to create a oversimplified webapp.

DJANGO CHANNELS
WEBSOCKETS
ASGI
CONSUMERS
CHANNEL LAYERS

DJANGO CHANNELS -> takes django and extends its ability Beyond HTTP to handle various protocols such as (chatprotocols,websockets,etc.)

CHANNELS -> Server Side

WEBSOCKETS -> Client Side

CHANNEL LAYERS -> Provide a way for multiple consumer instances to talk to each other, and other parts of django.
it consists of two terminologies:
Groups, Channels

groups -> example chat rooms (stored in inmemory database)
channels -> representing a user messagebox (mail box)



Steps to setup a server and create a socket connection:

1. Configure ASGI
2. Consumers
3. Routing 
4. WebSockets

set up basic django project:

now for real-time communication, install channels:

pip install channels

add channels to top of the installed apps in settings.py and add 
ASGI_APPLICATION = 'mywebsite.asgi.application' # project_name.asgi.application

now to integrate channels, open asgi.py:

from channels.routing import ProtocolTypeRouter
application = ProtocolTypeRouter({
    'http':get_asgi_application()
}) 


now crete a listener for the website in lobby.html,

now create a consumers.py file in your app.

CONSUMERS -> consumers are the channel's version of django views, except for they do more than just respond to request from the client,

they can also initiate the requests, all while keeping an open connection


now after writing the consumers.py we have to use it in routing, so create a routing.py

after all this, install:
pip install channels[daphne]

it is an ASGI-compatible server, (Django's built-in runserver isn't WebSocket-capable.)

TILL HERE YOU HAVE COMPLETED ONE PART THAT IS, YOUR MESSAGE IS VISIBLE BETWEEN SERVER AND YOURSELF.


NOW TO BROADCAST OR TO MAKE IT VISIBLE TO EVERYONE YOU HAVE TO USE CHANNEL LAYER

open settings.py add:

CHANNEL_LAYERS = {
    'default':{
        'BACKEND':'channels.layers.InMemoryChannelLayer'
    }
}

using InMemoryChannelLayer for development purposes, we have to integrate redis for production env.


now open consumers.py and import async to sync
from asgiref.sync import async_to_sync