from datetime import datetime, timedelta

import pytest

from pytest_django.asserts import assertTemplateUsed

from students.models import Logger, Student
from students.tasks import delete_logs, generate_random_students


@pytest.mark.django_db
class TestStudentModelRelatedViews:

    def test_create_student_view(self, client, create_student):
        response = client.get('/create-student/')
        assert response.status_code == 200
        assertTemplateUsed(response, 'students/create_student_form.html')
        response = client.post('/create-student/', data={'first_name': 'Name', 'last_name': 'Surname',
                                                         'age': 24, 'phone_number': '380000000000'},
                               follow=True)
        assert Student.objects.count() == 2
        assert Student.objects.get(pk=2).first_name == 'Name'
        assert Student.objects.get(pk=2).last_name == 'Surname'

        assert response.status_code == 200
        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]

        assert redirect_url == '/all-students/'
        assert redirect_status_code == 302

    def test_all_students_view(self, client, create_student):
        response = client.get('/all-students/')
        assert response.status_code == 200
        student = Student.objects.get(pk=1)
        assert student.first_name in response.content.decode()
        assertTemplateUsed(response, 'students/students_list.html')

    def test_edit_student_view(self, client, create_student):
        student = Student.objects.get(pk=1)
        response = client.get(f'/edit-student/{student.pk}/')
        assert response.status_code == 200
        assertTemplateUsed(response, 'students/student_edit_form.html')
        response = client.post(f'/edit-student/{student.pk}/',
                               data={'first_name': 'Name', 'last_name': 'Surname',
                                     'age': 24, 'phone_number': '380000000000'},
                               follow=True)
        assert response.status_code == 200
        assert Student.objects.get(pk=1).first_name == 'Name'
        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]

        assert redirect_url == '/all-students/'
        assert redirect_status_code == 302

    def test_delete_student_view(self, client, create_student):
        student = Student.objects.get(pk=1)
        response = client.get(f'/delete-student/{student.pk}/', follow=True)

        assert response.status_code == 200
        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]

        assert redirect_url == '/all-students/'
        assert redirect_status_code == 302


def test_main_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'students/index.html')


@pytest.mark.django_db
def test_generate_students_view_get(client):
    response = client.get('/generate-students/', {'count': 0})
    assert '<h1>Default value is 0</h1>'\
           '<br>Enter positive number from 1 too 100' == response.content.decode()
    response = client.get('/generate-students/', {'count': 100}, follow=True)
    assert Student.objects.count() == 100
    assert response.status_code == 200

    redirect_url = response.redirect_chain[0][0]
    redirect_status_code = response.redirect_chain[0][1]
    assert redirect_url == '/all-students/'
    assert redirect_status_code == 302


@pytest.mark.django_db
def test_generate_random_students(create_student):
    assert generate_random_students(3) == '3 random students created with success!'
    assert Student.objects.count() == 4


def test_admin_panel_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


def test_custom_error_404(client):
    response = client.get('/non-existent-url/')
    assert response.status_code == 404
    assertTemplateUsed(response, './errors/404_error_handler.html')


@pytest.mark.django_db
def test_handler_capitalize_student_fullname(client, create_student):
    student = Student.objects.get(pk=1)
    client.post(f'/edit-student/{student.pk}/', data={'first_name': 'mad', 'last_name': 'max', 'age': 22})

    assert Student.objects.get(pk=1).first_name == 'Mad'
    assert Student.objects.get(pk=1).last_name == 'Max'


@pytest.mark.django_db
def test_delete_logs(admin_client):
    assert Logger.objects.count() == 0
    admin_client.get('/admin/')
    assert Logger.objects.count() == 1
    log = Logger.objects.filter(
        created__lte=datetime.now() - timedelta(days=7)
    )
    assert log.count() == 0
    delete_logs()
