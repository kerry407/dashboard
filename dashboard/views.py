
from django.shortcuts import render
from .models import Account, Payment, ContactForm, About, WalletForm, WalletAddress
from user.models import UserProfile
from django.contrib import messages
from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='login')
def account(request):
    
    if request.method == 'POST':
        walletform = WalletForm(request.POST)
        if walletform.is_valid():
            Wallet = walletform.save(commit=False)
            Wallet.owner = request.user
            walletform.save()
            messages.success(request, 'Your wallet details has been successfully added')
            return redirect('account')
        else:
            messages.error('Please Try again later!')
    else:
        walletform = WalletForm()
    
    user_account = Account.objects.all()
    profile= UserProfile.objects.filter(user_id=request.user.id).first()
    
    context = {
        'account': user_account,
        'profile': profile,
        'wallet_form': walletform,
    }
    return render(request, 'dashboard/account.html', context)

def payment(request):
    payment_type = Payment.objects.all()
    
    context = {
        'payment_type': payment_type,
    }
    return render(request, 'dashboard/deposit.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team will reach you soon.")
            return redirect('contact')
        else:
            messages.error(request, 'Error sending message')
            return redirect('contact')
    else:
        form = ContactForm()
        
            
    about = About.objects.get(pk=1)
       
    context= { 
              
            'form': form,
            'about': about,
        }

    return render(request, 'dashboard/contact.html', context)

