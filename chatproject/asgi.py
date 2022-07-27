"""
ASGI config for chatproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from app_one.routing import urlpatterns
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(urlpatterns)
})
