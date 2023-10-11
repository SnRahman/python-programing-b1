from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email','image')
    # list_display = ('id','first_name', 'last_name', 'email','image')


admin.site.register(Student,StudentAdmin)