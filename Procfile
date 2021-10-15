web: gunicorn django_kornilov.wsgi:application --log-file -
worker: celery -A django_kornilov worker -l info -B
