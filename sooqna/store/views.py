from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse
from .forms.userform import SignupForm
from .forms.orderform import OrderForm
from .forms.userupdateform import UserUpdateForm
from .forms.passwordupdateform import PasswordUpdateForm
from .models import Product, Cart, Category

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
            return redirect('shop')
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
    categories = Category.objects.all()
    category_name = ''
    return render(request,'shop.html',{'products':products , 'categories': categories,'category_name':category_name})

def category_products(request,id):
    category_object = Category.objects.get(pk=id)
    category_name = category_object.name
    products = Product.objects.filter(category = category_object )

    categories = Category.objects.all()
    return render(request,'shop.html',{'products':products ,'categories': categories,'category_name':category_name})

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
            cart_item = Cart.objects.get(product = product,order_id=0)
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
    cart_items = Cart.objects.filter(user=request.user,order_id=0)
    grand_total = 0

    for cart in cart_items:
        grand_total += cart.sub_total 
    
    return render(request, 'show-cart.html',{'cart_items':cart_items, 'grand_total':grand_total})

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid:
            form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error generated')
        return redirect('edit_profile')
    else:
        form = UserUpdateForm(instance=request.user)

    # return HttpResponse(form)
    return render(request, 'edit-profile.html', {'form': form})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PasswordUpdateForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!

            messages.success(request, 'Password Changed Successfully')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Error generated')
            return redirect('change_password')
    else:
        form = PasswordUpdateForm(request.user)
    return render(request,'change-password.html', {'form': form})


def checkout(request):
    cart_items = Cart.objects.filter(user=request.user,order_id=0)
    grand_total = 0

    for cart in cart_items:
        grand_total += cart.sub_total

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:

            form_order = form.save(commit=False)
            if request.user is not None:
                form_order.user = request.user

            if request.POST.get('order_amount'):
                form_order.order_amount = request.POST.get('order_amount')
    
            if request.POST.get('mod'):
                form_order.payment_mode = request.POST.get('mod')

            form_order.save()

            cart_items = Cart.objects.filter(user=request.user,order_id=0)

            for cart_item in cart_items:
                cart_item.order_id = form_order.id
                cart_item.save()
                
            messages.success(request,'Order is Placed')
            return redirect('shop')
            # return HttpResponse(form_order.id)
        
        else:
            messages.error(request,'Something went wrong. try again with valid info.')
            return redirect('shop')
            # return HttpResponse(form.errors)

    else:
        form = OrderForm()

    return render(request, 'checkout.html',{'cart_items':cart_items, 'grand_total':grand_total, 'form': form})

def about(request):
    return render(request, 'about.html')