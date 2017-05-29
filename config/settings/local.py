# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

import socket
import os
from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='oc5n$2%17!J!fioi@f%jF5v^uuOyS6N9VtLL>/r[w[|6$l4E0]')

# Mail settings
# ------------------------------------------------------------------------------

# EMAIL_PORT = 1025

# EMAIL_HOST = 'localhost'
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
#                     default='django.core.mail.backends.console.EmailBackend')


# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 25
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

ANYMAIL = {
    "SENDGRID_API_KEY": "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",
}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + '1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', 'anymail', ]

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['.ngrok.io', 'localhost', 'rt-ord2-adzcer.c9users.io', ]

# DATABASE_URL="postgres://developer:pandaserverako@127.0.0.1:5432/bcast_online_report_dashboard"

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'bcast_online_report_dashboard',
    #     'USER': 'acercado',
    #     'PASSWORD': 'isf4laxi',
    # },
    # 'pandaserver': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'ord',
    #     'USER': 'ord_admin',
    #     'PASSWORD': 'ord_admin',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'c9',
        'USER': 'adzcer',
    },
}