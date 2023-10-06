from django.contrib import admin
from .models import Student
from .models import Test_table
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','email')

admin.site.register(Student,StudentAdmin)

admin.site.register(Test_table)