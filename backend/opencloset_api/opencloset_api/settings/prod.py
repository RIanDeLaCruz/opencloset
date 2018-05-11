from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.environ.setdefault('DJANGO_DB_ENGINE', ''),
        'NAME': os.environ.setdefault('DJANGO_DB_NAME', ''),
        'USER': os.environ.setdefault('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.setdefault('DJANGO_DB_PASSWORD', ''),
        'HOST': os.environ.setdefault('DJANGO_DB_HOST', ''),
        'PORT': os.environ.setdefault('DJANGO_DB_PORT', ''),
        'ATOMIC_REQUESTS': True,
    }
}

SECRET_KEY = os.environ.setdefault('DJANGO_SECRET_KEY', SECRET_KEY)
