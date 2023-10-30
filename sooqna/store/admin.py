from django.contrib import admin
from .models import Category, Product, Cart, Order

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('id','name','price','description','image','category')

class AdminCart(admin.ModelAdmin):
    list_display = ('id','user','sub_total','qty','product')

class AdminOrder(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','address','email','phone','grand_total')


admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Cart,AdminCart)
admin.site.register(Order)

