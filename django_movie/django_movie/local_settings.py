import os.path
from pathlib import Path


# SECURITY WARNING: keep the secret key used in production secret!
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-yeesc6=*)29!jj%+qy2y&1m5bz#eoqz5oi4a31ed8tp#2d=9@&'

DEBUG = True

ALLOWED_HOSTS = [
    '192.168.1.41',
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'movie.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
