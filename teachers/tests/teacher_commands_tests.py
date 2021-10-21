from django.core.management import call_command

from group.models import Group

import pytest

from students.models import Student

from teachers.models import Teacher


@pytest.mark.django_db
def test_console_command():
    args = ['1']
    options = {}
    call_command('generate-teachers', *args, **options)
    assert Teacher.objects.count() == 1
    assert 1 <= Student.objects.count() <= 10
    assert Group.objects.count() == 1
