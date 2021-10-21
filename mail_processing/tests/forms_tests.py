from mail_processing.forms import ContactUsForm


class TestContactUsForm:
    def test_form_is_valid(self):
        form = ContactUsForm(data={'contact_name': 'Yevhen', 'title': 'test title',
                                   'message': 'test message', 'email_from': 'testmail@mail.com'})
        assert form.is_valid()

    def test_form_is_invalid(self):
        form = ContactUsForm(data={'contact_name': 'Yevhen', 'title': 'test title',
                                   'message': 'test message', 'email_from': 'wrong email format'})
        assert not form.is_valid()

    def test_empty_form(self):
        form = ContactUsForm(data={})
        assert not form.is_valid()
