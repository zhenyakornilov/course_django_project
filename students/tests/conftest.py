import pytest

from .factories import LoggerFactory, StudentFactory


@pytest.fixture
@pytest.mark.django_db
def create_student():
    student = StudentFactory.create()
    return student


@pytest.fixture
@pytest.mark.django_db
def create_log():
    log = LoggerFactory.create()
    return log
