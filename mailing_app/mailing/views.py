from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from pytils.translit import slugify
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.db.utils import IntegrityError

from itertools import zip_longest
import datetime

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs
from mailing.forms import MailingSettingsForm, MailingMessageForm, ClientForm
from mailing.services import send_email


class MailingSettingsCreate(CreateView, LoginRequiredMixin):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        message_formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.last_sent = timezone.localtime()
        self.object.owner = self.request.user
        self.object.save()
        if message_formset.is_valid():
            message_formset.instance = self.object
            message_formset.save()
            # Если рассылка созданна со временем старта раньше текущего времени
            # и её статус не завершен, меняем статус и отправляем письмо
            if self.object.time <= timezone.localtime().time() and self.object.status != 'COMP':
                self.object.status = 'STAR'
                send_email(client_data=self.object.client.all(), mailing_settings=self.object,
                           mailing_message=self.object.mailingmessage)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(MailingSettings, MailingMessage,
                                               form=MailingMessageForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)
        return context_data


class MailingSettingsList(ListView):
    model = MailingSettings


class MailingSettingsDetail(DetailView):
    model = MailingSettings


class MailingSettingsUpdate(UpdateView, LoginRequiredMixin):
    pass


class MailingSettingsDelete(DeleteView, LoginRequiredMixin):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailing_list')


class ClientCreate(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.email)
            new_client.save()
        return super().form_valid(form)


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client


class ClientUpdate(UpdateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.email)
            new_client.save()
        return super().form_valid(form)


class ClientDelete(DeleteView, LoginRequiredMixin):
    model = Client
    success_url = reverse_lazy('mailing:clients_list')


class MailingLogsList(ListView):
    model = MailingLogs
