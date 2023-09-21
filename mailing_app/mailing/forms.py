from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from pytils.translit import slugify

from mailing.models import Client, MailingSettings, MailingMessage


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = 'owner', 'slug'

    def clean(self):
        cleaned_data = self.cleaned_data.get('email')
        for client in Client.objects.all():
            if slugify(cleaned_data) == client.slug:
                raise forms.ValidationError('Клиент с данным email уже существует')
            return self.cleaned_data


class TimeInput(forms.DateInput):
    input_type = 'time'


class MailingSettingsForm(forms.ModelForm):

    class Meta:
        model = MailingSettings
        exclude = 'last_sent', 'status', 'logs', 'owner'
        widgets = {
            'time': TimeInput()
        }


class MailingMessageForm(forms.ModelForm):

    class Meta:
        model = MailingMessage
        fields = '__all__'
