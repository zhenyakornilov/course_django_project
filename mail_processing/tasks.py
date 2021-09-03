from celery import shared_task

from django.core.mail import EmailMessage

from django_kornilov.settings import ADMINS_EMAIL, EMAIL_HOST_USER


@shared_task
def proceed_contact_us_form(contact_name, title, message, email_from):
    if email_from not in ADMINS_EMAIL:
        text_to_sender = f'Hello, {contact_name}!\nWe have received Your message: \n\t{message}'
        email = EmailMessage(
            subject=title,
            body=text_to_sender,
            from_email=f'DJANGO_KORNILOV {EMAIL_HOST_USER}',
            to=[email_from, ]
        )
        email.send()
    text_to_admins = f'Received an e-mail from: {email_from}\n\t{message}'
    email = EmailMessage(
        subject=title,
        body=text_to_admins,
        from_email=f'DJANGO_KORNILOV {EMAIL_HOST_USER}',
        to=ADMINS_EMAIL
    )
    email.send()

    return 'An e-mail has been sent!'
