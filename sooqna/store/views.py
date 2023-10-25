from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.http import HttpResponse
from .forms.userform import SignupForm

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

def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # return HttpResponse(form.errors)
        if form.is_valid:
            form.save()
            messages.success(request,'Registered Successfully!!! kindy login')
            return redirect('login')

        else:
            messages.error(request,'Something went wrong. try again with valid info.')
            return redirect('signup')
    else:
        form = SignupForm()
        return render(request,'signup.html',{'form':form})

def edit_profile(request):
    return render(request, 'edit-profile.html')

def product_detalis(request):
    return render(request,'product-details.html')

def show_cart(request):
    return render(request, 'show-cart.html')

def checkout(request):
    return render(request, 'checkout.html')