from django.urls import path

from main_page.apps import MainPageConfig
from main_page.views import MainPageView


app_name = MainPageConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]