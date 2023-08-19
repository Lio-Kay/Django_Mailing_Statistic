from django.db import models

from mailing_app.mailing.apps import MailingConfig

app_name = MailingConfig.name

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronim = models.CharField(max_length=50, **NULLABLE,verbose_name='Отчество')
    email = models.EmailField(max_length=100,verbose_name='Контактный email')
    commentary = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}'

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'клиенты'
        ordering = 'name',  'surname', 'email'

class MailingSettings(models.Model):
    time = models.DateTimeField(verbose_name='Время рассылки')
    DAILY = "DLY"
    WEEKLY = "WKL"
    MONTHLY = "MTH"
    FREQUENCY_CHOICES = [
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
    ]
    frequency = models.CharField(max_length=3, choices=FREQUENCY_CHOICES, default=DAILY, verbose_name='Переодичность')
    COMPLETED = "COMP"
    CREATED = "CRE"
    STARTED = "STAR"
    STATUS_CHOICES = [
        (COMPLETED, "Completed"),
        (CREATED, "Created"),
        (STARTED, "Started"),
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=CREATED,  verbose_name='Статус')
    client = models.ForeignKey(to='Client', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.time}, {self.frequency}, {self.status}, {self.client}'

    class Meta:
        verbose_name = 'настройку'
        verbose_name_plural = 'настройки'
        ordering = 'time',  'frequency', 'status',

class MailingMessage(models.Model):
    subject = models.CharField(max_length=200,verbose_name='Тема')
    message = models.TextField(**NULLABLE,verbose_name='Сообщение')
    settings = models.ForeignKey(to=MailingSettings, **NULLABLE, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.subject}, {self.message}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = 'subject',

class MailingLogs(models.Model):
    time = models.DateTimeField(verbose_name='Время последней попытки')
    COMPLETED = "COMP"
    CREATED = "CRE"
    STARTED = "STAR"
    STATUS_CHOICES = [
        (COMPLETED, "Completed"),
        (CREATED, "Created"),
        (STARTED, "Started"),
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус')
    service_response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')
    settigns = models.ForeignKey(to=MailingSettings, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.time}, {self.status}, {self.service_response}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = 'time', 'status'
