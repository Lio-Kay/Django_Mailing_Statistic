from django.urls import path

from mailing_app.main_page.apps import MainPageConfig
from mailing_app.main_page.views import MainPageView


app_name = MainPageConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]