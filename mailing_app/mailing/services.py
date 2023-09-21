from smtplib import SMTPException

from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.timezone import now

from config import settings
from mailing.models import MailingLogs, MailingSettings
from time import sleep


def send_email(client_data, mailing_settings, mailing_message):
    """Отправляет сообщения и создает логи по рассылке"""
    for client in client_data:
        try:
            send_mail(
                subject=mailing_message.subject,
                message=mailing_message.message,
                from_email=None,
                recipient_list=[client.email],
                fail_silently=False
            )
            MailingLogs.objects.create_log(time=now(), status='SUCC', settings=mailing_settings)
            mailing_settings.save()
        except SMTPException as exeption:
            MailingLogs.objects.create_log(time=now(), status='FAIL', service_response=exeption.args[0])
            sleep(20)
            try:
                send_mail(
                    subject=mailing_message.subject,
                    message=mailing_message.message,
                    from_email=None,
                    recipient_list=[client.email],
                    fail_silently=False
                )
            except SMTPException as exeption:
                MailingLogs.objects.create_log(time=now(), status='FAIL', service_response=exeption.args[0])
