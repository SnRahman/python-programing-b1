from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'Name: {self.name}'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, default='')
    image = models.ImageField(upload_to='store/products/')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    sub_total = models.DecimalField(default=0,decimal_places=2,max_digits=8)
    
    def __str__(self):
        return super().__str__()