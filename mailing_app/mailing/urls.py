from django.urls import path

from mailing_app.mailing.apps import MailingConfig
from mailing_app.mailing.views import (MailingSettingsCreate, MailingSettingsList, MailingSettingsDelete,
                                       ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete)


app_name = MailingConfig.name

urlpatterns = [
    path('create_mailng', MailingSettingsCreate.as_view(), name='mailing_create'),
    path('', MailingSettingsList.as_view(), name='mailing_list'),
    path('delete_mailing/<int:pk>', MailingSettingsDelete.as_view(), name='mailing_delete'),
    path('create_client', ClientCreate.as_view(), name='client_create'),
    path('clients', ClientList.as_view(), name='clients_list'),
    path('client_details/<int:pk>', ClientDetail.as_view(), name='client_details'),
    path('client_update/<int:pk>', ClientUpdate.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDelete.as_view(), name='client_delete'),
]
