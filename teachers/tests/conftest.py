import pytest

from .factories import TeacherFactory


@pytest.fixture
@pytest.mark.django_db
def create_teacher():
    teacher = TeacherFactory.create()
    return teacher
