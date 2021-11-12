from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "age", "phone_number",
                    "get_group_id", "get_group_name")
    list_filter = ("age", "last_name", 'first_name')
    search_fields = ("last_name__startswith",)

    def get_group_id(self, obj):
        return f"Group ID: {obj.group.id}"
    get_group_id.short_description = 'Group ID'

    def get_group_name(self, obj):
        return obj.group.group_name
    get_group_name.short_description = 'Group name'
