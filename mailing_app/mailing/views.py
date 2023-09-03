from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse

from mailing.models import Client, MailingSettings, MailingMessage, MailingLogs
from mailing_app.mailing.forms import MailingSettingsForm

from itertools import zip_longest


class ClientCreate(CreateView):
    pass


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        try:
            mailing_settings_pk = MailingSettings.objects.filter(client=cd.get('object').pk)[0].pk
            cd['mailing_info'] = (
                zip_longest(list(MailingSettings.objects.filter(client=cd.get('object').pk)),
                            list(MailingMessage.objects.filter(settings=mailing_settings_pk))))
        except IndexError:
            cd['mailing_info'] = (
                zip_longest(list(MailingSettings.objects.filter(client=cd.get('object').pk))))

        cd['mailing_counter'] = len((MailingSettings.objects.filter(client=cd.get('object').pk)))

        return cd

class ClientUpdate(UpdateView):
    model = Client
    fields = 'name', 'surname', 'patronim', 'email', 'commentary'

    def form_valid(self, form):
        if form.is_valid():
            updated_user = form.save()
            updated_user.slug = slugify(f'{updated_user.name}_{updated_user.surname}_{updated_user.patronim}')
            updated_user.save()
        return super().form_valid(form)


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients_list')


class MailingSettingsCreate(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:clients_list')

