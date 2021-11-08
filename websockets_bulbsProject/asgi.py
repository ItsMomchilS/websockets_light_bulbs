import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from light_bulb.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tic_tac_toe.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websockets': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})
