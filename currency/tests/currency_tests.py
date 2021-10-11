from currency.tasks import get_currency_rates

import pytest

from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_currency_rates(client):
    assert get_currency_rates() == 'Currencies saved'
    response = client.get('/currency/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'currency/currency_list.html')
