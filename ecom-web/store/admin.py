from django.contrib import admin
from .models import Category, Customer, Product, Order, ProductMedia
# Register your models here.

class ProductMediaAdmin(admin.TabularInline):
    model = ProductMedia

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone','email','password')

class ProductAdmin(admin.ModelAdmin):
    # inlines = [ProductMediaAdmin,]
    list_display = ('name','price','category','description','image')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','customer','quantity','address','phone','date','status')

admin.site.register(Category)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
