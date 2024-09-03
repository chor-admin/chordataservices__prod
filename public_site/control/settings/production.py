'''
Development settings are development specfic settings that build on
the Common settings file
'''
import os
import mimetypes

#Import modules
from control.settings.common import *
from utilities.azure_key_vault import GetSecret


# SECURITY WARNING: keep the secret key used in production secret!
v_call_secret_key=GetSecret("django-prod-secret")
SECRET_KEY = v_call_secret_key.fxCallSecret()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['chordataservices.com','www.chordataservices.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
v_call_database=GetSecret("db-name-prod")
v_call_user=GetSecret("srvcs-account-name")
v_call_password=GetSecret("srvcs-passcode")
v_call_host=GetSecret("prod-host-ip")
v_call_port=GetSecret("prod-host-port")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': '-c search_path=django_system,public'},
        'NAME': v_call_database.fxCallSecret(),
        'USER': v_call_user.fxCallSecret(),
        'PASSWORD': v_call_password.fxCallSecret(),
        'HOST': v_call_host.fxCallSecret(),
        'PORT': v_call_port.fxCallSecret(),
    },

    'data': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': '-c search_path=django_data,public'},
        'NAME': v_call_database.fxCallSecret(),
        'USER': v_call_user.fxCallSecret(),
        'PASSWORD': v_call_password.fxCallSecret(),
        'HOST': v_call_host.fxCallSecret(),
        'PORT': v_call_port.fxCallSecret(),
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

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'