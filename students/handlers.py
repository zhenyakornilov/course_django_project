from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def capitalize_first_last_name(sender, **kwargs):
    print('TEST')
