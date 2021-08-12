from django import forms


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student\'s first name', required=True, max_length=200)
    last_name = forms.CharField(label='Student\'s last name', required=True, max_length=200)
    age = forms.IntegerField(label='Student\'s age', required=True)
