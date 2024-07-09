import os
import environ
import mimetypes

from control.settings.common import *
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('PROD_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.chordataservices.com']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': '-c search_path=django_system,public'},
        'NAME': env('PROD_DB_NAME'),
        'USER': env("PROD_DB_USER"),
        'PASSWORD': env("PROD_DB_PASSWORD"),
        'HOST': env("PROD_DB_HOST"),
        'PORT': env("PROD_DB_PORT"),
    },

    'data': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': '-c search_path=django_data,public'},
        'NAME': env('PROD_DB_NAME'),
        'USER': env("PROD_DB_USER"),
        'PASSWORD': env("PROD_DB_PASSWORD"),
        'HOST': env("PROD_DB_HOST"),
        'PORT': env("PROD_DB_PORT"),
    }
}

#HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

#HSTS settings
SECURE_HSTS_SECONDS = 600 # 10 Min
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

mimetypes.add_type("text/css", ".css", True)

STATIC_URL = '/static/'
STATIC_ROOT = [BASE_DIR / 'staticfiles']
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = [BASE_DIR / 'media']
