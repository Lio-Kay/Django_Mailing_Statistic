from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (MailingSettingsCreate, MailingSettingsList, MailingSettingsDetail, MailingSettingsDelete, finish_mailing, start_mailing,
                                       ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete, MailingLogsList)


app_name = MailingConfig.name

urlpatterns = [
    path('create_mailng', MailingSettingsCreate.as_view(), name='mailing_create'),
    path('', cache_page(10)(MailingSettingsList.as_view()), name='mailing_list'),
    path('mailing_detail/<int:pk>', MailingSettingsDetail.as_view(), name='mailing_details'),
    path('delete_mailing/<int:pk>', MailingSettingsDelete.as_view(), name='mailing_delete'),
    path('finish_mailing/<int:pk>', finish_mailing, name='finish_mailing'),
    path('start_mailing/<int:pk>', start_mailing, name='start_mailing'),
    path('create_client', ClientCreate.as_view(), name='client_create'),
    path('clients', cache_page(10)(ClientList.as_view()), name='clients_list'),
    path('client_details/<int:pk>', ClientDetail.as_view(), name='client_details'),
    path('client_update/<int:pk>', ClientUpdate.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDelete.as_view(), name='client_delete'),
    path('mailing_logs', cache_page(5)(MailingLogsList.as_view()), name='mailing_logs_list'),
]
