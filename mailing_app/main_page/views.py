from django.shortcuts import render
from django.views.generic import View
from django.core.cache import cache

from random import choices

from blog.models import BlogPost
from mailing.models import MailingSettings, Client
from config.settings import CACHE_ENABLED



class MainPageView(View):
    template_name = 'main_page/main.html'

    def get(self, request):
        mailing_total_counter = len(MailingSettings.objects.all())
        mailing_active_counter = len(MailingSettings.objects.filter(status='STAR'))
        clients_counter = len(Client.objects.all())

        if CACHE_ENABLED:
            key = 'blogpost_list'
            blogpost_list = cache.get(key)
            if blogpost_list is None:
                blogpost_list = BlogPost.objects.all()
                cache.set(key, blogpost_list)
        else:
            blogpost_list = BlogPost.objects.all()

        try:
            blogpost_list = choices(blogpost_list, k=3)
        except IndexError:
            pass
        context = {
            'mailing_total_counter': mailing_total_counter,
            'mailing_active_counter': mailing_active_counter,
            'clients_counter': clients_counter,
            'blogpost_list': blogpost_list,
        }
        return render(request, self.template_name, context)