from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete


app_name = MailingConfig.name

urlpatterns = [
    path('', ClientList.as_view(), name='list_clients'),
    path('<int:pk>', ClientDetail.as_view(), name='client_details'),
    path('create', ClientCreate.as_view(), name='create_client'),
    path('<int:pk>', ClientUpdate.as_view(), name='update_client'),
    path('<int:pk>', ClientUpdate.as_view(), name='delete_client'),
]
