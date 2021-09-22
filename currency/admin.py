from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("created_at", "currency", "source", "price_for_buy", "price_for_sell")
    list_filter = ("created_at", "source", "currency", )
    search_fields = ("source",)
