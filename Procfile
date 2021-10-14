web: gunicorn django_kornilov.wsgi --log-file -
worker: celery -A django_kornilov worker --beat --concurrency 5 -l info
# beat: celery -A django_kornilov beat
