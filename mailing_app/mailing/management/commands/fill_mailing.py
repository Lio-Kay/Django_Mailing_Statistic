from django.core.management import BaseCommand

from mailing_app.mailing.models import Client, MailingSettings, MailingMessage, MailingLogs


class Command(BaseCommand):

    def handle(self, *args, **options):

        new_clients = {}
        new_mailingsettings = {}
        new_mailingmessage = {}
        new_mailinglogs = {}

        Client.objects.all().delete()
        MailingSettings.objects.all().delete()
        MailingMessage.objects.all().delete()
        MailingLogs.objects.all().delete()

        for client in new_clients:
            Client.objects.create(**client)
        for setting in new_mailingsettings:
            MailingSettings.objects.create(**setting)
        for message in new_mailingmessage:
            Client.objects.create(**message)
        for log in new_mailinglogs:
            Client.objects.create(**log)

        self.stdout.write(self.style.SUCCESS('Successfully deleted all data and filled the model with new data.'))
