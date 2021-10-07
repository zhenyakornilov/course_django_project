import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Student


def validate_phone_number(form_phone_number):
    if not re.match(r"^380\d{9}$", form_phone_number):
        raise ValidationError(f'{form_phone_number}: Enter phone number in 380xxxxxxxxx format')


class StudentForm(forms.ModelForm):
    phone_number = forms.CharField(label='Student\'s phone', required=False,
                                   empty_value=None, validators=[validate_phone_number],
                                   widget=forms.TextInput(attrs={'placeholder': '380xxxxxxxxx'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'phone_number']


class GenerateStudentsForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(500)
        ]
    )
