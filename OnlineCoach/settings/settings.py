from .base import *

# Settings used on official environments

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG_MODE'] in ['True', True]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(' ')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
    }
}

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# TODO: Insert Sentry configuration
