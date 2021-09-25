import pytest

from django import urls

from ..models import Student, Logger

from ..tasks import generate_random_students

from faker import Faker

fake = Faker()


@pytest.fixture()
def student_model_data():
    print('HELLO')
    return {'first_name': f'{fake.first_name()}', 'last_name': f'{fake.last_name()}', 'age': fake.random_int(18, 26)}


@pytest.mark.django_db
def test_generate_students_task(student_model_data):
    assert Student.objects.count() == 0
    Student.objects.create(**student_model_data)
    assert Student.objects.count() == 1


