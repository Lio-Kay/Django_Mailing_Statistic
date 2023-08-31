# Generated by Django 4.2.4 on 2023-08-19 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronim', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=100, verbose_name='Контактный email')),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('name', 'surname', 'email'),
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Время рассылки')),
                ('frequency', models.CharField(choices=[('DLY', 'Daily'), ('WKL', 'Weekly'), ('MTH', 'Monthly')], default='DLY', max_length=3, verbose_name='Переодичность')),
                ('status', models.CharField(choices=[('COMP', 'Completed'), ('CRE', 'Created'), ('STAR', 'Started')], default='CRE', max_length=4, verbose_name='Статус')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
                'ordering': ('time', 'frequency', 'status'),
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailingsettings')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
                'ordering': ('subject',),
            },
        ),
        migrations.CreateModel(
            name='MailingLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Время последней попытки')),
                ('status', models.CharField(choices=[('COMP', 'Completed'), ('CRE', 'Created'), ('STAR', 'Started')], default='CRE', max_length=4, verbose_name='Статус')),
                ('service_response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('settigns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логги',
                'ordering': ('time', 'status'),
            },
        ),
    ]
