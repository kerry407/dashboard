from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2']
        
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email 
            raise forms.ValidationError('Email {} is already in use'.format(email))
    
                                        
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username 
            raise forms.ValidationError('Username {} is already in use. Try a different one.'.format(username))

    
