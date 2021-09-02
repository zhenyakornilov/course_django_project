from celery import shared_task

from django.core.mail import EmailMessage

from django_kornilov.settings import RECIPIENTS_EMAIL


@shared_task
def proceed_contact_us_form(title, message, email_from):
    text = f'Received a message from: {email_from} \n\t{message}'
    email = EmailMessage(
        title,
        text,
        'DJANGO_KORNILOV <email_from>',
        [],
        RECIPIENTS_EMAIL,
        reply_to=[email_from],
        headers={'Message-ID': 'foo'},
    )
    email.send()
    return 'An e-mail has been sent!'
