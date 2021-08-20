import re

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Student


@receiver(pre_save, sender=Student)
def capitalize_first_last_name(sender, **kwargs):
    print('TEST')


@receiver(pre_save, sender=Student)
def format_phone_number(sender, **kwargs):
    if phone_number := kwargs['instance'].phone_number:
        kwargs['instance'].phone_number = re.sub(r"\D", "", phone_number)
