# Generated by Django 4.2.4 on 2023-09-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_client_owner_mailingsettings_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'ordering': ('time', 'frequency', 'status'), 'permissions': [('disable_mailing', 'Can disable mailing')], 'verbose_name': 'настройку', 'verbose_name_plural': 'настройки'},
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='client',
            field=models.ManyToManyField(limit_choices_to={'owner': True}, to='mailing.client'),
        ),
    ]
