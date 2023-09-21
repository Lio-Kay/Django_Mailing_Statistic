from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.utils import timezone

import datetime

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs
from mailing.services import send_email


def my_job():
    mailing_settings = MailingSettings.objects.all()
    for setting in mailing_settings:
        if setting.frequency == 'DLY':
            if timezone.now() - datetime.timedelta(days=1) >= setting.last_sent:
                send_email(client_data=setting.client.all(), mailing_settings=setting, mailing_message=setting.mailingmessage)
                setting.last_sent = timezone.localtime()
                setting.save()

        elif setting.frequency == 'WKL':
            if timezone.now() - datetime.timedelta(days=7) >= setting.last_sent:
                send_email(client_data=setting.client.all(), mailing_settings=setting, mailing_message=setting.mailingmessage)
                setting.last_sent = timezone.localtime()
                setting.save()

        elif setting.frequency == 'MTH':
            if timezone.now() - datetime.timedelta(days=30) >= setting.last_sent:
                send_email(client_data=setting.client.all(), mailing_settings=setting, mailing_message=setting.mailingmessage)
                setting.last_sent = timezone.localtime()
                setting.save()


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )

        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
