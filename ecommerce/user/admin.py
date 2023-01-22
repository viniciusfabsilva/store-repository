from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'birth_date')
    search_fields = ('email', 'first_name')


admin.site.register(User, UserAdmin)
