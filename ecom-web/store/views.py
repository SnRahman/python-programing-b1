from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    products = Product.objects.all()
    # return HttpResponse('home')
    return render(request,'index.html',{'products':products})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,('login successfull!'))
            return redirect('home')
        else:
            messages.success(request,('There is some error kindly login again.'))
            return redirect('login')
    else:
        return render(request,'login.html')

def user_logout(request):
    pass