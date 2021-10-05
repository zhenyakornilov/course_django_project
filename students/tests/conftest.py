import pytest

from .factories import StudentFactory


@pytest.fixture
@pytest.mark.django_db
def create_student():
    student = StudentFactory.create()
    return student
