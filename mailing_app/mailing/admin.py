from django.contrib import admin

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'surname', 'patronim', 'email', 'commentary', 'slug'
    list_display_links = 'id', 'name', 'surname', 'patronim', 'email'
    search_fields = 'name', 'surname',  'email',


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = 'id', 'time', 'frequency', 'status', 'client'
    list_display_links = 'id', 'time'
    list_filter = 'frequency', 'status',
    search_fields = 'time', 'client',
    list_editable = 'frequency', 'status',


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = 'id', 'subject', 'message', 'settings'
    list_display_links = 'id', 'subject', 'message', 'settings'
    search_fields = 'subject', 'message',


@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = 'id', 'time', 'status', 'service_response'
    list_filter = 'status',
    search_fields = 'time', 'service_response',
