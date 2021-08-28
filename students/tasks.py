from datetime import datetime, timedelta

from celery import shared_task

from faker import Faker

from .models import Logger, Student

fake = Faker()


@shared_task
def generate_random_students(total):
    result = []

    for i in range(total):
        result.append(Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.random_int(18, 26)
        ))
    Student.objects.bulk_create(result)

    return f'{total} random students created with success!'


@shared_task
def delete_logs():
    logs = Logger.objects.filter(created__lte=datetime.now() - timedelta(days=7)).all()
    if not logs:
        return 'Logs older than 7 days not found'
    else:
        logs.delete()
        return 'Logs deleted!'
