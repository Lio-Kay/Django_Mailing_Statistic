# Generated by Django 4.2.4 on 2023-08-31 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_rename_setting_mailingmessage_settings_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailinglogs',
            old_name='settigns',
            new_name='settings',
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='logs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.mailinglogs'),
        ),
    ]
