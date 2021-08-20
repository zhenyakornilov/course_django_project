from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Teacher


@receiver(pre_save, sender=Teacher)
def capitalize_student_fullname(sender, **kwargs):
    if first_name := kwargs['instance'].first_name:
        kwargs['instance'].first_name = first_name.capitalize()
    if last_name := kwargs['instance'].last_name:
        kwargs['instance'].last_name = last_name.capitalize()
