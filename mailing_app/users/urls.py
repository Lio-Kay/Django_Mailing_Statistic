from django.urls import path

from mailing_app.users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    # path('', .as_view(), name=''),
]