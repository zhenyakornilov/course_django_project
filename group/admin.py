from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name", "students_in_group")
    list_filter = ("group_name", )
    search_fields = ("group_name__startswith", )
