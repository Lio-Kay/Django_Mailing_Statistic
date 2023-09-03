# Generated by Django 4.2.4 on 2023-08-31 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_remove_mailingmessage_settings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingmessage',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings'),
        ),
    ]
