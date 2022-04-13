from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def debug():
    from time import sleep
    print('Start')
    sleep(10)
    print('End')


@shared_task
def send_registration_email(email_to):
    from time import sleep
    sleep(10)
    print('Send Email')
    send_mail(
        'Django LMS Registration',
        'Test Message.',
        settings.EMAIL_HOST_USER,
        [email_to],
        fail_silently=False,
    )