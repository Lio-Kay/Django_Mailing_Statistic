from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'text', 'views', 'publication_date'
    list_display_links = 'id', 'title', 'text', 'views', 'publication_date'
    search_fields = 'title', 'publication_date'
