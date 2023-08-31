from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from mailing_app.mailing.models import Client, MailingSettings, MailingMessage, MailingLogs


class ClientCreate(CreateView):
    pass


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
   pass


class ClientUpdate(UpdateView):
    pass


class ClientDelete(DeleteView):
    pass

