from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = 'title', 'text', 'views', 'publication_date'
    list_display_links = 'title', 'text', 'views', 'publication_date'
    search_fields = 'title', 'publication_date'
