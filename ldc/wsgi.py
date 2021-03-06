"""
WSGI config for ldc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import os, sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ldc.settings")

application = get_wsgi_application()

path = '/n/sw/www/portal'
if path not in sys.path:
    sys.path.append(path)
