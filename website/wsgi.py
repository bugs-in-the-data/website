"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

#activate_this = '/var/www/html/website/biodiversityenv/bin/activate_this.py'
#exec(compile(open(activate_this,"rb").read(),activate_this, 'exec'), dict(__file__=activate_this))

application = get_wsgi_application()
