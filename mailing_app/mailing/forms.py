from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from mailing.models import Client, MailingSettings, MailingMessage


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = 'slug',


class MailingSettingsForm(forms.ModelForm):

    class Meta:
        model = MailingSettings
        exclude = 'logs',


class MailingMessageForm(forms.ModelForm):

    class Meta:
        model = MailingMessage
        fields = '__all__'
