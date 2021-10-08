import pytest

from students.forms import GenerateStudentsForm, StudentForm


class TestStudentForm:
    def test_form_is_invalid(self):
        form = StudentForm(data={'first_name': 'test', 'last_name': 'test',
                                 'age': 24, 'phone_number': 'bad_number'})
        assert not form.is_valid()

    @pytest.mark.django_db
    def test_form_is_valid(self):
        form = StudentForm(data={'first_name': 'test', 'last_name': 'test',
                                 'age': 24, 'phone_number': '380000000000'})
        assert form.is_valid()

    def test_phone_validation(self):
        form = StudentForm(data={'first_name': 'test', 'last_name': 'test',
                                 'age': 24, 'phone_number': '355663809280'})
        assert not form.is_valid()

    def test_form_is_empty(self):
        form = StudentForm(data={})
        assert not form.is_valid()
        assert len(form.errors) == 3


class TestGenerateStudentsForm:
    def test_min_value_validator(self):
        form = GenerateStudentsForm(data={'total': 9})
        assert not form.is_valid()

    def test_max_value_validator(self):
        form = GenerateStudentsForm(data={'total': 600})
        assert not form.is_valid()

    def test_correct_count(self):
        form = GenerateStudentsForm(data={'total': 200})
        assert form.is_valid()

    def test_empty_form(self):
        form = GenerateStudentsForm(data={})
        assert not form.is_valid()
        assert len(form.errors) == 1
