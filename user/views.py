from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages 
from django.contrib.auth import login, logout, authenticate
from .decorators import unauthenticated_user
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from dashboard.models import WalletAddress
from dashboard.models import Account
# Create your views here.

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = UserProfile(user=myuser)
            acc = Account(account_name=myuser)
            p.first_name = myuser.first_name
            p.last_name = myuser.last_name
            p.save()
            acc.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account for {email} has been created, you can now login')
            return redirect('login')
        else:
            messages.error(request, form.errors)
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'user/register.html', context)

@unauthenticated_user
def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.info(request, f'Username Or Password is incorrect')

    return render(request, 'user/login.html')

@login_required(login_url='register')
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userprofile(request):
    
    profile= UserProfile.objects.filter(user_id=request.user.id).first()

    context = {
        'profile': profile,
    }

    return render(request, 'user/userprofile.html', context)

def change_password(request):
    if request.method == 'POST':
        passwordform = PasswordChangeForm(request.user, request.POST)
        if passwordform.is_valid():
            user = passwordform.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password has been changed successfully')
            return redirect('change_password')
        else:
            messages.error(request, passwordform.errors)
    else:
        passwordform = PasswordChangeForm(request.user)
    
    return render(request, 'user/password_change.html', {'password_form': passwordform})
            