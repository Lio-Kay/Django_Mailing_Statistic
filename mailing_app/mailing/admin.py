from django.contrib import admin

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'surname', 'patronim', 'email', 'commentary', 'slug', 'owner'
    list_display_links = 'id', 'name', 'surname', 'patronim', 'email', 'commentary', 'slug', 'owner'
    search_fields = 'id', 'name', 'surname', 'email'


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = 'id', 'time', 'last_sent', 'frequency', 'status', 'owner'
    list_display_links = 'id', 'time', 'owner'
    list_filter = 'frequency', 'status'
    search_fields = 'id', 'time',
    list_editable = 'last_sent', 'frequency', 'status'


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = 'id', 'subject', 'message', 'settings'
    list_display_links = 'id', 'subject', 'message', 'settings'
    search_fields = 'id', 'subject', 'message'


@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = 'id', 'time', 'status', 'service_response'
    list_filter = 'status',
    search_fields = 'id', 'time', 'service_response'
