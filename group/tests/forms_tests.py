from group.forms import GroupForm


class TestGroupForm:

    def test_form_is_valid(self):
        form = GroupForm(data={'group_name': 'Math', 'students_in_group': 10})
        assert form.is_valid()

    def test_form_is_invalid(self):
        form = GroupForm(data={'group_name': 'Math', 'students_in_group': 'not number'})
        assert not form.is_valid()

    def test_empty_form(self):
        form = GroupForm(data={})
        assert not form.is_valid()
