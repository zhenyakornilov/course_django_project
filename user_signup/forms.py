from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Enter a valid email.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use. "
                                        "Please supply a different email address.")
        return email


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class PasswordCustomChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Current password',
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-control', 'type': 'password', 'style': 'width:250px'}
                                   ))
    new_password1 = forms.CharField(label='New password',
                                    max_length=100,
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'type': 'password', 'style': 'width:250px'}
                                    ))
    new_password2 = forms.CharField(label='Confirm new password',
                                    max_length=100,
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'type': 'password', 'style': 'width:250px'}
                                    ))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class SetPasswordCustomForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New password',
                                    max_length=100,
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'type': 'password', 'style': 'width:250px'}
                                    ))
    new_password2 = forms.CharField(label='Confirm new password',
                                    max_length=100,
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'type': 'password', 'style': 'width:250px'}
                                    ))

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
