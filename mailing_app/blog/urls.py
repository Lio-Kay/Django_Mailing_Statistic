from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogPostDetail


app_name = BlogConfig.name

urlpatterns = [
    path('<int:pk>', BlogPostDetail.as_view(), name='blogpost_details'),
]
