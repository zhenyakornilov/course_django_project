from django.test import Client

import pytest

from students.models import Student
from students.tasks import generate_random_students


@pytest.mark.django_db
def test_new_student(create_student):
    assert Student.objects.count() == 1
    c = Client()
    get_main = c.get('/all-students/')
    assert get_main.status_code == 200
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_main_page(create_student):
    c = Client()
    get_main = c.get('/')
    assert get_main.status_code == 200
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_generate_students():
    assert generate_random_students(3) == '3 random students created with success!'
    assert Student.objects.count() == 3
