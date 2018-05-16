from .base import *
import django_heroku

django_heroku.settings(locals(), allowed_hosts=False)

DEBUG = True
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['fruering-qa.herokuapp.com']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:
    from .local import *
except ImportError:
    pass
