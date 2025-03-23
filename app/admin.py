from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['id','last_name','first_name', 'username', 'user_type']

    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff', 'user_type']

admin.site.register(CustomUser, UserModel)
admin.site.register(Organization)
admin.site.register(Region)
admin.site.register(School_Year)