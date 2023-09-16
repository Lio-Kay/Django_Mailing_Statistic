from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now

from itertools import zip_longest

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs
from mailing.forms import MailingSettingsForm, MailingMessageForm, ClientForm
from mailing.services import send_email


class MailingSettingsCreate(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        message_formset = self.get_context_data()['formset']
        self.object = form.save()
        if message_formset.is_valid():
            message_formset.instance = self.object
            message_formset.save()
            if self.object.time <= now():
                send_email(client_data=self.object.client.all(), mailing_settings=self.object, mailing_message=self.object.mailingmessage)
            else:
                self.object.status = 'Инициирована'

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingSettings, MailingMessage, form=MailingMessageForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)
        return context_data


class MailingSettingsList(ListView):
    model = MailingSettings


class MailingSettingsDetail(DetailView):
    model = MailingSettings


class MailingSettingsUpdate(UpdateView):
    pass


class MailingSettingsDelete(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailing_list')

class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients_list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.email)
            new_client.save()
        return super().form_valid(form)


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.email)
            new_client.save()
        return super().form_valid(form)


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients_list')


class MailingLogsList(ListView):
    model = MailingLogs


# class ClientDetail(DetailView):
#     model = Client
#
#     def get_context_data(self, **kwargs):
#         cd = super().get_context_data(**kwargs)
#         try:
#             mailing_settings_pk = MailingSettings.objects.filter(client=cd.get('object').pk)[0].pk
#             cd['mailing_info'] = (
#                 zip_longest(list(MailingSettings.objects.filter(client=cd.get('object').pk)),
#                             list(MailingMessage.objects.filter(settings=mailing_settings_pk))))
#         except IndexError:
#             cd['mailing_info'] = (
#                 zip_longest(list(MailingSettings.objects.filter(client=cd.get('object').pk))))
#
#         cd['mailing_counter'] = len((MailingSettings.objects.filter(client=cd.get('object').pk)))
#
#         return cd
