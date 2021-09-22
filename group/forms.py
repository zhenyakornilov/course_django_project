from django import forms

from .models import Group


class GroupForm(forms.ModelForm):
    group_name = forms.CharField(label='Group name', required=True, max_length=200)
    students_in_group = forms.IntegerField(label='Count of students in group')

    class Meta:
        model = Group
        fields = ['group_name', 'students_in_group']
