from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from threading import current_thread
from multiprocessing import current_process


@shared_task
def debug_io():
    from time import sleep
    print('Start')
    sleep(10)
    print('End')


@shared_task
def debug_cpu():
    n = 50_000_000
    while n != 0:
        n -= 1

@shared_task
def send_registration_email(email_to):
    # from time import sleep
    # sleep(10)
    print('Send Email')
    send_mail(
        'Django LMS Registration',
        'Test Message.',
        settings.EMAIL_HOST_USER,
        [email_to],
        fail_silently=False,
    )


@shared_task
def parse_binance():
    print('Start Parsing...')


@shared_task
def parse_kraken():
    print('Start Parsing...')


@shared_task
def parse_nexo():
    print('Start Parsing...')