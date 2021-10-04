from django.contrib import admin

# Register your models here.
from .models import UserAccount


@admin.register(UserAccount)
class AdminUserAccount(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','is_active','is_staff','created_at']
