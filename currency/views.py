from django.views.generic.list import ListView

from .models import Currency


class CurrencyListView(ListView):
    model = Currency

