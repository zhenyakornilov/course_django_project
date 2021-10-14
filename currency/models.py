from django.db import models


class Currency(models.Model):
    CURRENCIES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('RUB', 'Ruble'),
    ]

    created_at = models.DateTimeField(auto_now=True, db_column='Creation date')
    currency = models.CharField(max_length=4, choices=CURRENCIES, db_column='Currency')
    source = models.CharField(max_length=20, db_column='Source')
    price_for_buy = models.DecimalField(max_digits=15, decimal_places=6, db_column='Buy price')
    price_for_sell = models.DecimalField(max_digits=15, decimal_places=6, db_column='Sell price')

    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.created_at}::{self.currency}, {self.source}; " \
               f"BUY:{self.price_for_buy}, SELL:{self.price_for_sell}"
