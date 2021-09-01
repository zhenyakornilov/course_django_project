from celery import shared_task

from django.core.mail import send_mail


@shared_task
def proceed_contact_us_form(title, message, email_from):
    send_mail(title,
              message,
              email_from,
              ['eugen-kornilov@ukr.net'],
              )

    return 'An e-mail has been sent!'
