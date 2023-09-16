from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (MailingSettingsCreate, MailingSettingsList, MailingSettingsDetail, MailingSettingsDelete,
                                       ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete, MailingLogsList)


app_name = MailingConfig.name

urlpatterns = [
    path('create_mailng', MailingSettingsCreate.as_view(), name='mailing_create'),
    path('', cache_page(10)(MailingSettingsList.as_view()), name='mailing_list'),
    path('mailing_detail/<int:pk>', cache_page(1)(MailingSettingsDetail.as_view()), name='mailing_detail'),
    path('delete_mailing/<int:pk>', MailingSettingsDelete.as_view(), name='mailing_delete'),
    path('create_client', ClientCreate.as_view(), name='client_create'),
    path('clients', cache_page(10)(ClientList.as_view()), name='clients_list'),
    path('client_details/<int:pk>', cache_page(1)(ClientDetail.as_view()), name='client_details'),
    path('client_update/<int:pk>', ClientUpdate.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDelete.as_view(), name='client_delete'),
    path('mailing_logs', cache_page(10)(MailingLogsList.as_view()), name='mailing_logs_list'),
]
