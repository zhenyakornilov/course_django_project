from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("subject", "last_name", "first_name", "age")
    list_filter = ("age", "last_name", "subject")
    search_fields = ("last_name__startswith", "first_name__startswith")
