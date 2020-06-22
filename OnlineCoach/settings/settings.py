from .base import *

# Settings used on official environments

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG_MODE'] in ['True', True]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# TODO: Change database to Postgres
# Database
# DATABASES = {
#     'default': {
#         'ENGINE':   'django.db.backends.oracle',
#         'NAME':     os.environ['DATABASE_DEFAULT_NAME'],
#         'USER':     os.environ['DATABASE_DEFAULT_USER'],
#         'PASSWORD': os.environ['DATABASE_DEFAULT_PASSWORD'],
#     }
# }
