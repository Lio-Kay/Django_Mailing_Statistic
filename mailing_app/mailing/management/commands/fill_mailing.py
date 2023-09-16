from django.core.management import BaseCommand

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs


class Command(BaseCommand):

    def handle(self, *args, **options):

        new_clients = [
            {"name":"Алексей",
            "surname":"Алексеевич",
            "patronim":"Алексеев",
            "email":"alex@mail.ru",
            "commentary":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,",
            "slug":"alexmailru"},
            {"name":"Андрей",
            "surname":"Андреевич",
            "patronim":"Андреев",
            "email":"andrey@gmail.com",
            "commentary":"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere",
            "slug":"andreygmailcom"},
            {"name":"Александр",
            "surname":"Александрович",
            "patronim":"Александров",
            "email":"alexandr@ya.ru",
            "commentary":"",
            "slug":"alexandryaru"},
            {"name":"Борис",
            "surname":"Борисович",
            "patronim":"Борисов",
            "email":"boris@mail.ru",
            "commentary":"Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles. Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan",
            "slug":"borismailru"},
            {"name":"Вадим",
            "surname":"Вадимович",
            "patronim":"Вадимов",
            "email":"vad@gmail.com",
            "commentary":"",
            "slug":"vadgmailcom"},
        ]

        new_mailingsettings = [
            {
            "time": "2023-09-19T17:00:00Z",
            "frequency": "DLY",
            "status": "CRE",
            "client": [
                3
            ]
            },
            {
            "time": "2023-09-20T17:00:00Z",
            "frequency": "DLY",
            "status": "CRE",
            "client": [
                3
            ]
            },
            {
            "time": "2023-09-18T17:00:00Z",
            "frequency": "DLY",
            "status": "CRE",
            "client": [
                3,
                1,
                2,
                4,
                5
            ]
            },
            {
            "time": "2023-09-18T17:00:00Z",
            "frequency": "WKL",
            "status": "CRE",
            "client": [
                2
            ]
            },
            {
            "time": "2023-09-18T17:00:00Z",
            "frequency": "MTH",
            "status": "CRE",
            "client": [
                4,
                5
            ]
            }
        ]

        new_mailingmessage = [
            {
            "subject": "Тема1",
            "message": "Сообщение1",
            "settings": 1
            },
            {
            "subject": "Тема2",
            "message": "Сообщение2",
            "settings": 2
            },
            {
            "subject": "Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3Тема3",
            "message": "Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3Сообщение3",
            "settings": 3
            },
            {
            "subject": "Тема4",
            "message": "Сообщение4",
            "settings": 4
            },
            {
            "subject": "Тема5",
            "message": "Сообщение5",
            "settings": 5
            }
        ]

        Client.objects.all().delete()
        MailingSettings.objects.all().delete()
        MailingMessage.objects.all().delete()

        for client in new_clients:
            Client.objects.create(**client)
        for setting in new_mailingsettings:
            MailingSettings.objects.create(**setting)
        for message in new_mailingmessage:
            Client.objects.create(**message)

        self.stdout.write(self.style.SUCCESS('Successfully deleted all data and filled the model with new data.'))
