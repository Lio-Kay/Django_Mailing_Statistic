from django.urls import path

from mailing_app.mailing.apps import MailingConfig
from mailing_app.mailing.views import ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete, MailingSettingsCreate


app_name = MailingConfig.name

urlpatterns = [
    path('', ClientList.as_view(), name='clients_list'),
    path('client/<int:pk>', ClientDetail.as_view(), name='client_details'),
    path('create_client', ClientCreate.as_view(), name='create_client'),
    path('update_client/<int:pk>', ClientUpdate.as_view(), name='update_client'),
    path('delete_client/<int:pk>', ClientDelete.as_view(), name='delete_client'),
    path('client/<int:pk>/create_mailing', MailingSettingsCreate.as_view(), name='create_mailing'),
]
