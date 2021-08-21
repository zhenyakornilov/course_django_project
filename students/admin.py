from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age")
    list_filter = ("age", "last_name", 'first_name')
    search_fields = ("last_name__startswith", )
