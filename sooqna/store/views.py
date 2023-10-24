from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('home')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=email , password =password )
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfull.')
            return redirect('login')
        else:
            messages.error(request,'Invalid credentials!!!')
            return redirect('login')    
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'logged out successfull.')
    return redirect('login')





def edit_profile(request):
    return render(request, 'edit-profile.html')

def product_detalis(request):
    return render(request,'product-details.html')

def show_cart(request):
    return render(request, 'show-cart.html')

def checkout(request):
    return render(request, 'checkout.html')