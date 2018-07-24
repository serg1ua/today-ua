"""
WSGI config for todayua project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# wsgi.py
import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

#todayua.settings.production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todayua.settings.local")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
