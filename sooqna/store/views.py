from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.http import HttpResponse
from .forms.userform import SignupForm
from .forms.orderform import OrderForm
from .models import Product, Cart

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


def shop(request):
    products = Product.objects.all()
    return render(request,'shop.html',{'products':products})

def product_detalis(request, id):
    product = Product.objects.get(pk=id)
    return render(request,'product-details.html',{'product':product})


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        qty = int(request.POST['qty'])  
        user = request.user
        product = Product.objects.get(pk=product_id)
        
        try:
            cart_item = Cart.objects.get(product = product)
        except:
            cart_item = False

        if cart_item is False:
            sub_total = qty * product.price
            cart = Cart(product= product, qty= qty,user=user,sub_total = sub_total)
            cart.save()
        else:
            cart_item.qty =  cart_item.qty + qty
            cart_item.sub_total = cart_item.qty * cart_item.product.price
            cart_item.save()
           
        messages.success(request,'product added successfully!')
        return redirect('checkout')
        # return HttpResponse(request.POST['qty'])
    

def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = 0

    for cart in cart_items:
        grand_total += cart.sub_total 
    
    return render(request, 'show-cart.html',{'cart_items':cart_items, 'grand_total':grand_total})

def edit_profile(request):
    return render(request, 'edit-profile.html')

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = 0

    for cart in cart_items:
        grand_total += cart.sub_total

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()

            form_order = form.save(commit=False)
            if request.user is not None:
                form_order.user = request.user

            if request.POST.get('order_amount'):
                form_order.order_amount = request.POST.get('order_amount')
    
            if request.POST.get('mod'):
                form_order.payment_mode = request.POST.get('mod')

            form.save()

            return HttpResponse(form_order)
        else:
            return HttpResponse(form.errors)

    else:
        form = OrderForm()

    return render(request, 'checkout.html',{'cart_items':cart_items, 'grand_total':grand_total, 'form': form})