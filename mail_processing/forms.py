from django import forms


class ContactUsForm(forms.Form):
    contact_name = forms.CharField(label='Your name', max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Enter Your name'}
                                   ))
    title = forms.CharField(label='Title', max_length=100)
    message = forms.CharField(max_length=2000,
                              widget=forms.Textarea(
                                  attrs={
                                      'placeholder': 'Enter Your message here',
                                      'rows': 10,
                                      'cols': 50
                                  }
                              ))
    email_from = forms.EmailField(max_length=100,
                                  widget=forms.EmailInput(
                                      attrs={'placeholder': 'example@mail.com'}))
