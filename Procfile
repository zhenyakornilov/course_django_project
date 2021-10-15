web: gunicorn django_kornilov.wsgi --log-file -
worker: python manage.py celery worker -B -l info
