from currency.tasks import get_currency_rates

from django.test import override_settings

import pytest

from pytest_django.asserts import assertTemplateUsed


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
@pytest.mark.django_db
def test_currency_rates(client):
    task = get_currency_rates.delay()
    assert task.successful()
    response = client.get('/currency/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'currency/currency_list.html')
