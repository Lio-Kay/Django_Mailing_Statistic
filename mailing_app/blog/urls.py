from django.urls import path

from mailing_app.blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    # path('', .as_view(), name=''),
]