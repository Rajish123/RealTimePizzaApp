"""
ASGI config for Pizza project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pizza.settings')

# application = get_asgi_application()

ws_pattern = []

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(
        ws_pattern
    ))
})
