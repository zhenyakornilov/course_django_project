from celery import shared_task

import requests

from .models import Currency


@shared_task
def get_currency_rates():
    currency_codes = (840, 978, 643)
    response_monobank = requests.get('https://api.monobank.ua/bank/currency')
    response_nbank = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

    for rate in response_monobank.json():
        if rate.get('currencyCodeA') not in [code for code in currency_codes]:
            continue
        elif rate.get('currencyCodeA') == currency_codes[0] and rate.get('currencyCodeB') not in currency_codes:
            letter_code = 'USD'
        elif rate.get('currencyCodeA') == currency_codes[1] and rate.get('currencyCodeB') not in currency_codes:
            letter_code = 'EUR'
        elif rate.get('currencyCodeA') == currency_codes[2] and rate.get('currencyCodeB') not in currency_codes:
            letter_code = 'RUB'
        currency_monobank = Currency(
            currency=str(letter_code),
            source='Monobank',
            price_for_buy=rate.get('rateBuy'),
            price_for_sell=rate.get('rateSell')
        )
        currency_monobank.save()

    for rate in response_nbank.json():
        if rate.get('cc') not in [currency[0] for currency in Currency.CURRENCIES]:
            continue
        currency_nbank = Currency(
            currency=rate.get('cc'),
            source='National Bank',
            price_for_buy=rate.get('rate'),
            price_for_sell=rate.get('rate')
            )
        currency_nbank.save()
