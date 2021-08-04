from django import forms


class TeacherForm(forms.Form):
    subject = forms.CharField(label='Subject', required=True, max_length=200)
    first_name = forms.CharField(label='First name', required=True, max_length=200)
    last_name = forms.CharField(label='Last name', required=True, max_length=200)
    age = forms.IntegerField(label='Age')
