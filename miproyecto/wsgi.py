"""
WSGI config for miproyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

os.environ['DJANGO_SETTINGS_MODULE']  = 'miproyecto.settings.local'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
