from django.urls import path

from mailing_app.main_page.apps import MainPageConfig


app_name = MainPageConfig.name

urlpatterns = [
    # path('', .as_view(), name=''),
]