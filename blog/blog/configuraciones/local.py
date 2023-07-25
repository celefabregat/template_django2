from .base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "blog",
        "USER": "julian",
        "PASSWORD": "julianbenitez1",
        "HOST": "localhost",
        "PORT": "3306",
    }
}