from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from .forms.registerForm import SignUpForm

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

def user_signup(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You Have Registered Successfully!! Welcome!"))
			return redirect('home')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})

def user_logout(request):
    pass