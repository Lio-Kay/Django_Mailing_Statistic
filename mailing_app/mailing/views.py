from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from pytils.translit import slugify
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.db.utils import IntegrityError
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

from itertools import zip_longest
import datetime

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs
from mailing.forms import MailingSettingsForm, MailingMessageForm, ClientForm
from mailing.services import send_email


class MailingSettingsCreate(LoginRequiredMixin, CreateView):
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


class MailingSettingsUpdate(LoginRequiredMixin, UpdateView):
    model = MailingSettings

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return self.object


class MailingSettingsDelete(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return self.object


def finish_mailing(request, pk):
    mailing = get_object_or_404(MailingSettings, id=request.POST.get('finish_mailing'))
    mailing.status = 'COMP'
    mailing.save()
    return HttpResponseRedirect(reverse('mailing:mailing_details', args=[str(pk)]))


def start_mailing(request, pk):
    mailing = get_object_or_404(MailingSettings, id=request.POST.get('start_mailing'))
    mailing.status = 'STAR'
    mailing.save()
    return HttpResponseRedirect(reverse('mailing:mailing_details', args=[str(pk)]))


class ClientCreate(LoginRequiredMixin, CreateView):
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


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return self.object

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.slug = slugify(new_client.email)
            new_client.save()
        return super().form_valid(form)


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return self.object


class MailingLogsList(ListView):
    model = MailingLogs
