
from django.contrib import admin
from . models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    

admin.site.register(UserProfile,UserProfileAdmin)