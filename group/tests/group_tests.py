import pytest

from pytest_django.asserts import assertTemplateUsed

from group.models import Group


@pytest.mark.django_db
def test_create_group_view(client):
    response = client.get('/create-group/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'group/create_group.html')

    response = client.post('/create-group/',
                           data={'group_name': 'Group name', 'students_in_group': 10},
                           follow=True)

    assert response.status_code == 200
    assert Group.objects.count() == 1
    assert Group.objects.get(pk=1).group_name == 'Group name'
    assert Group.objects.get(pk=1).students_in_group == 10

    redirect_url = response.redirect_chain[0][0]
    redirect_status_code = response.redirect_chain[0][1]
    assert redirect_url == '/all-groups/'
    assert redirect_status_code == 302


@pytest.mark.django_db
def test_all_groups_view(client):
    response = client.get('/all-groups/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'group/group_list.html')
    assert Group.objects.count() == 0
