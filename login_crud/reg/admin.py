from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'city')