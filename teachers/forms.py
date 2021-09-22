from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):
    subject = forms.CharField(label='Subject', required=True, max_length=200)
    first_name = forms.CharField(label='First name', required=True, max_length=200)
    last_name = forms.CharField(label='Last name', required=True, max_length=200)
    age = forms.IntegerField(label='Age')

    class Meta:
        model = Teacher
        fields = ['subject', 'first_name', 'last_name', 'age']
