from locale import currency
from django.db import models
from django.contrib.auth.models import User 
from django.forms import ModelForm, Select
# Create your models here.

class Account(models.Model):
    account_name = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    active_deposit = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    total_profit = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    transaction_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.account_name.first_name
    
class Payment(models.Model):
    currency = models.CharField(max_length=30)
    font_link = models.CharField(max_length=100, default='None')
    shorthand = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.currency
    

class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WalletAddress(models.Model):
    currency_type = models.CharField(max_length=10)
    wallet_address = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.owner.first_name
 


class WalletForm(ModelForm):

      
    class Meta:
        CURRENCY = [
        ('Bitcoin', 'Bitcoin'),
        ('Ethereum', 'Ethereum'),
        ]
        model = WalletAddress
        fields = ['title', 'currency_type', 'wallet_address']
        
        widgets = {
            'currency_type': Select(attrs={'class': 'form-control', 'placeholder': 'Crypto-Currency'}, choices=CURRENCY),
        }
         

class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class About(models.Model):
    about = models.TextField(blank=True)