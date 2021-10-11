import pytest

from pytest_django.asserts import assertTemplateUsed

from teachers.models import Teacher


@pytest.mark.django_db
class TestStudentModelRelatedViews:

    def test_create_teacher_view(self, client, create_teacher):
        response = client.get('/create-teacher/')
        assert response.status_code == 200
        assertTemplateUsed(response, 'teachers/create_teacher_form.html')

        response = client.post('/create-teacher/', data={'subject': 'Math', 'first_name': 'Name',
                                                         'last_name': 'Surname', 'age': 24},
                               follow=True)
        assert response.status_code == 200
        assert Teacher.objects.count() == 2
        assert Teacher.objects.get(pk=2).first_name == 'Name'
        assert Teacher.objects.get(pk=2).last_name == 'Surname'

        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]
        assert redirect_url == '/all-teachers/'
        assert redirect_status_code == 302

    def test_all_teachers_view(self, client, create_teacher):
        response = client.get('/all-teachers/')
        assert response.status_code == 200
        assert Teacher.objects.get(pk=1).first_name in response.content.decode()
        assertTemplateUsed(response, 'teachers/teachers_list.html')

    def test_edit_teacher_view(self, client, create_teacher):
        teacher = Teacher.objects.get(pk=1)
        response = client.get(f'/edit-teacher/{teacher.pk}')
        assert response.status_code == 200
        assertTemplateUsed(response, 'teachers/teacher_edit_form.html')

        response = client.post(f'/edit-teacher/{teacher.pk}',
                               data={'subject': 'Math', 'first_name': 'Name', 'last_name': 'Surname', 'age': 24},
                               follow=True)
        assert response.status_code == 200
        assert Teacher.objects.get(pk=1).first_name == 'Name'

        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]
        assert redirect_url == '/all-teachers/'
        assert redirect_status_code == 302

    def test_delete_teacher_view(self, client, create_teacher):
        teacher = Teacher.objects.get(pk=1)
        response = client.post(f'/delete-teacher/{teacher.pk}', follow=True)
        assert response.status_code == 200

        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]
        assert redirect_url == '/all-teachers/'
        assert redirect_status_code == 302


@pytest.mark.django_db
def test_handler_capitalize_teacher_fullname(client, create_teacher):
    teacher = Teacher.objects.get(pk=1)
    client.post(f'/edit-teacher/{teacher.pk}',
                data={'subject': 'Math', 'first_name': 'good', 'last_name': 'teacher', 'age': 22})
    assert Teacher.objects.get(pk=1).first_name == 'Good'
    assert Teacher.objects.get(pk=1).last_name == 'Teacher'
