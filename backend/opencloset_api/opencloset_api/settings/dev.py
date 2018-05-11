from .base import *
import os


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'opencloset_db',
        'USER': 'opencloset',
        'PASSWORD': 'opencloset',
        'HOST': 'localhost',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}

SECRET_KEY = '(4)^7p2c$%)x8_*!8724vn-jh4@2w#mpl2cnjcaul3h01(ee%6'
MEDIA_URL = '/'
MEDIA_ROOT = '/Volumes/Storage/Freelance/opencloset/backend/opencloset_api'
