from django.shortcuts import render
from django.views.generic import DetailView


from blog.models import BlogPost


class BlogPostDetail(DetailView):
    model = BlogPost
