from django.contrib import admin
from .models import Category, Product

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('id','name','price','description','image')

admin.site.register(Product,AdminProduct)
admin.site.register(Category)

