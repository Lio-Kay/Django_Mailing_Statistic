from django import forms

from mailing.models import MailingSettings


class DateInput(forms.DateInput):
    input_type = 'date'


class MailingSettingsForm(forms.ModelForm):

    class Meta:
        model = MailingSettings
        exclude = 'logs',
        widgets = {
            'made_on': DateInput()
        }

