from django.apps import AppConfig


class TeachersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teachers'

    def ready(self):
        from .handlers import capitalize_student_fullname  # noqa: F401
