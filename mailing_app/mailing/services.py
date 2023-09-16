from smtplib import SMTPException

from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.timezone import now

from config import settings
from mailing.models import MailingLogs


def send_email(client_data, mailing_settings, mailing_message):
    try:
        for client in client_data:
            send_mail(
                subject=mailing_message.subject,
                message=mailing_message.message,
                from_email=None,
                recipient_list=[client.email],
                fail_silently=False
            )
            MailingLogs.objects.create_log(time=now(), status='Успешно')
    except SMTPException as exeption:
        MailingLogs.objects.create_log(time=now(), status='Ошибка', service_response=exeption.args[0])
    else:
        mailing_settings.status = 'Завершена'
