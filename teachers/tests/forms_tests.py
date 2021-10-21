from teachers.forms import TeacherForm


class TestTeacherForm:
    def test_form_is_invalid(self):
        form = TeacherForm(data={'first_name': 'test', 'last_name': 'test', 'age': 24})
        assert not form.is_valid()

    def test_form_is_valid(self):
        form = TeacherForm(data={'subject': 'Math', 'first_name': 'test',
                                 'last_name': 'test', 'age': 24})
        assert form.is_valid()

    def test_form_is_empty(self):
        form = TeacherForm(data={})
        assert not form.is_valid()
        assert len(form.errors) == 4
