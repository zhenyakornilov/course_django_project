from django.test import override_settings

from mail_processing.tasks import proceed_contact_us_form

from pytest_django.asserts import assertTemplateUsed


class TestShowContactFormView:

    def test_get_contact_form(self, client):
        response = client.get('/contact-us/')
        assert response.status_code == 200
        assertTemplateUsed(response, 'mail_processing/contact_us_form.html')

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_send_email(self, client):
        test_data = {'contact_name': 'Yevhen', 'title': 'test title',
                     'message': 'test message', 'email_from': 'testmail@mail.com'}
        response = client.post('/contact-us/', data=test_data)
        assert response.status_code == 302
        task = proceed_contact_us_form.delay(contact_name=test_data.get('contact_name'),
                                             title=test_data.get('title'),
                                             message=test_data.get('message'),
                                             email_from=test_data.get('email_from'))
        assert task.result == 'An e-mail has been sent!'
        assert task.successful()
