from django.contrib import admin
from .models import *
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_name']
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['currency', 'address']
    
class WalletAddressAdmin(admin.ModelAdmin):
    list_display = ['owner','currency_type']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email', 'subject','message','status', 'note')
    readonly_fields = ('name', 'subject','email', 'message')
    list_filter= ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email', 'subject','message','status', 'note')
    list_per_page = 20

class AboutAdmin(admin.ModelAdmin):
    list_display=('about',)
    
admin.site.register(Account, AccountAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WalletAddress, WalletAddressAdmin)
