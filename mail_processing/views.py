from django.contrib import messages
from django.shortcuts import render

from .forms import ContactUsForm
from .tasks import proceed_contact_us_form


def show_contact_form(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            proceed_contact_us_form.delay(
                title=form.cleaned_data.get('title'),
                message=form.cleaned_data.get('message'),
                email_from=form.cleaned_data.get('email_from')
            )

            messages.success(request, 'An e-mail has been sent!')

    else:
        form = ContactUsForm()

    return render(request, 'mail_processing/contact_us_form.html', {'form': form})
