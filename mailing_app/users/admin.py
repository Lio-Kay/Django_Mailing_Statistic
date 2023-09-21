from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'conformation_code'
    list_display_links = 'id', 'first_name', 'last_name', 'email', 'conformation_code'
    search_fields = 'email',
