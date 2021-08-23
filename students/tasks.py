from celery import shared_task

from faker import Faker

from .models import Student

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
