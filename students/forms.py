import re

from django import forms
from django.core.exceptions import ValidationError


def validate_phone_number(form_phone_number):
    if any(char.isalpha() for char in form_phone_number):
        raise ValidationError('Enter numbers only!')
    elif not re.match(r"^380\d{9}$", re.sub(r"\D", "", form_phone_number)):
        raise ValidationError('Enter phone number in +38(0xx)-xxx-xx-xx format')


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student\'s first name', required=True, max_length=200)
    last_name = forms.CharField(label='Student\'s last name', required=True, max_length=200)
    age = forms.IntegerField(label='Student\'s age', required=True)
    phone_number = forms.CharField(label='Student\'s phone', required=False,
                                   empty_value=None, validators=[validate_phone_number],
                                   widget=forms.TextInput(attrs={'placeholder': '+38(0xx)-xxx-xx-xx'}))
