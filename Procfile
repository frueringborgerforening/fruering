release: python manage.py migrate
web: gunicorn fruering.wsgi --log-file - --log-level $LOG_LEVEL
