from django.urls import path

from mailing_app.mailing.apps import MailingConfig
from mailing_app.mailing.views import ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete, MailingSettingsCreate, MailingSettingsUpdate, MailingSettingsDelete


app_name = MailingConfig.name

urlpatterns = [
    path('', ClientList.as_view(), name='clients_list'),
    path('client/<slug:slug>', ClientDetail.as_view(), name='client_details'),
    path('create_client', ClientCreate.as_view(), name='create_client'),
    path('update_client/<slug:slug>', ClientUpdate.as_view(), name='update_client'),
    path('delete_client/<slug:slug>', ClientDelete.as_view(), name='delete_client'),
    path('client/<slug:slug>/create_mailing', MailingSettingsCreate.as_view(), name='create_mailing'),
    path('client/<slug:slug>/update_mailing', MailingSettingsUpdate.as_view(), name='update_mailing'),
    path('client/<slug:slug>/delete_mailing', MailingSettingsDelete.as_view(), name='delete_mailing'),
]
