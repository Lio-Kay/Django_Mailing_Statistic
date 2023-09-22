from django.shortcuts import render
from django.views.generic import View
from django.core.cache import cache

from random import choice

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
            blogpost_list_3_publications = []
            while len(blogpost_list_3_publications) < 3:
                item = choice(blogpost_list)
                if item not in blogpost_list_3_publications:
                    blogpost_list_3_publications.append(item)
        except IndexError:
            pass
        context = {
            'mailing_total_counter': mailing_total_counter,
            'mailing_active_counter': mailing_active_counter,
            'clients_counter': clients_counter,
            'blogpost_list': blogpost_list_3_publications,
            'blogpost': BlogPost.objects.all(),
        }
        return render(request, self.template_name, context)


def handler400(request, exception=None):
    response = render(request, "main_page/templates/errors/404.html", context={}, status=400)
    return response

def handler403(request, exception=None):
    response = render(request, "main_page/templates/errors/404.html", context={}, status=403)
    return response


def handler404(request, exception=None):
    response = render(request, "main_page/templates/errors/404.html", context={}, status=404)
    return response



def handler500(request, exception=None):
    response = render(request, "main_page/templates/errors/404.html", context={}, status=500)
    return response
