from django.contrib import admin

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'name', 'surname', 'patronim', 'email', 'commentary'
    search_fields = 'name', 'surname',  'email'


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = 'time', 'frequency', 'status', 'client'
    list_filter = 'frequency', 'status',
    search_fields = 'time', 'client',


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = 'subject', 'message', 'settings'
    search_fields = 'subject', 'message',

@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = 'time', 'status', 'service_response',
    list_filter = 'status',
    search_fields = 'time', 'service_response',
