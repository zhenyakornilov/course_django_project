from django import forms


class ContactUsForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1500,
                              widget=forms.Textarea(
                                  attrs={
                                      'placeholder': 'Enter Your message here',
                                      'rows': 10,
                                      'cols': 50
                                  }
                              ))
    email_from = forms.EmailField(max_length=100)
