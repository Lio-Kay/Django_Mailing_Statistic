from django.db import models

from mailing_app.config import settings
from mailing.apps import MailingConfig


app_name = MailingConfig.name

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель клиента сервиса"""
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronim = models.CharField(**NULLABLE, max_length=50, verbose_name='Отчество')
    email = models.EmailField(max_length=100,verbose_name='Контактный email')
    commentary = models.TextField(**NULLABLE, verbose_name='Комментарий')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}'

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'клиенты'
        ordering = 'name',  'surname', 'email'


class MailingSettings(models.Model):
    """Модель настроек рассылки"""
    time = models.TimeField(verbose_name='Время рассылки')
    last_sent = models.DateTimeField(**NULLABLE, verbose_name='Время до отправки')
    DAILY = "DLY"
    WEEKLY = "WKL"
    MONTHLY = "MTH"
    FREQUENCY_CHOICES = [
        (DAILY, "Ежедневно"),
        (WEEKLY, "Еженедельно"),
        (MONTHLY, "Ежемесячно"),
    ]
    frequency = models.CharField(max_length=3, choices=FREQUENCY_CHOICES, default=DAILY, verbose_name='Переодичность')
    COMPLETED = "COMP"
    CREATED = "CRE"
    STARTED = "STAR"
    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Инициирована"),
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='CRE',  verbose_name='Статус')
    client = models.ManyToManyField(to='Client')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Владелец')

    def __str__(self):
        return f'{self.time}, {self.last_sent}, {self.frequency}, {self.status}'

    class Meta:
        verbose_name = 'настройку'
        verbose_name_plural = 'настройки'
        ordering = 'time',  'frequency', 'status',


class MailingMessage(models.Model):
    """Модель сообщения рассылки"""
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    settings = models.OneToOneField(**NULLABLE, to='MailingSettings', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}, {self.message}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = 'subject',


class MailingLogsManager(models.Manager):
    """Класс для создания логов для модели логов"""
    def create_log(self, time, status, settings, service_response=None):
        log = self.create(time=time, status=status, settings=settings, service_response=service_response)

        return log


class MailingLogs(models.Model):
    """Модель логов"""
    time = models.DateTimeField(verbose_name='Время последней попытки')
    SUCCESFUL = "SUCC"
    FAILED = "FAIL"
    STATUS_CHOICES = [
        (SUCCESFUL, "Успешно"),
        (FAILED, "Ошибка"),
    ]
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default=SUCCESFUL, verbose_name='Статус')
    service_response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')
    settings = models.ForeignKey(to='MailingSettings', on_delete=models.CASCADE)

    objects = MailingLogsManager()

    def __str__(self):
        return f'{self.time}, {self.status}, {self.service_response}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = 'time', 'status'
