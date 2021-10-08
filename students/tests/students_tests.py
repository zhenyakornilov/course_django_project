import pytest

from pytest_django.asserts import assertTemplateUsed, assertFormError

from students.forms import StudentForm
from students.models import Student
from students.tasks import generate_random_students


@pytest.mark.django_db
@pytest.mark.parametrize('path', [
    '/',
    '/all-students/',
    '/edit-student/'
])
def test_students_views(path, client, create_student):
    if path == '/edit-student/':
        student = Student.objects.get(pk=1)
        path = f'/edit-student/{student.pk}/'
        response = client.post(path, data={'first_name': 'test', 'last_name': 'test',
                                           'age': 24, 'phone_number': '380000000000'},
                               follow=True)
        redirect_url = response.redirect_chain[0][0]
        print(redirect_url)
        redirect_status_code = response.redirect_chain[0][1]

        assert redirect_url == '/all-students/'
        assert redirect_status_code == 302

    response = client.get(path)
    assert response.status_code == 200
    if path == '/':
        assertTemplateUsed(response, 'students/index.html')
    if path == '/all-students/':
        student = Student.objects.get(pk=1)
        assert student.first_name in response.content.decode()
        assertTemplateUsed(response, 'students/students_list.html')
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_edit_student_view(request, client, create_student):
    response_get = client.get('/edit-student/1/')
    # assertTemplateUsed(response_get, 'students/student-edit-form.html')
    # invalid_data = {'first_name': 'test', 'last_name': 'test',
    #                 'age': 24, 'phone_number': 'bad_number'}
    # expected_error = f"{invalid_data.get('phone_number')}: Enter phone number in 380xxxxxxxxx format"
    # form = StudentForm()
    # response = client.post('/edit-student/1/', data=invalid_data)
    # assertFormError(response, form, 'phone_number', expected_error)


@pytest.mark.django_db
def test_edit_student(client, create_student):
    response = client.get('/edit-student/1/')
    assert response.status_code == 200
    # assertTemplateUsed(response, 'students/student_edit_form.html')
    # form = StudentForm()
    # invalid_data = {'first_name': 'test', 'last_name': 'test', 'age': 24, 'phone_number': 'bad_number'}
    # expected_error = f'{invalid_data.get("phone_number")}: Enter phone number in 380xxxxxxxxx format'
    # response_edit = client.post('/edit-student/1/', data=invalid_data)
    # assertFormError(response, form, 'phone_number', expected_error)


@pytest.mark.django_db
def test_generate_random_students(create_student):
    assert generate_random_students(3) == '3 random students created with success!'
    assert Student.objects.count() == 4


def test_admin_panel_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


class TestStudentCreationForm:
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


def test_custom_error_404(client):
    response = client.get('/non-existent-url/')
    assert response.status_code == 404
    assertTemplateUsed(response, './errors/404_error_handler.html')
