from django import forms


class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', required=True, max_length=200)
    students_in_group = forms.IntegerField(label='Count of students in group')
