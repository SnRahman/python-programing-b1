from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def index(request):
    return HttpResponse('index')

# def create_student(request):
#     return render(request,'form.html')

# def register(request):
#     return request


def create(request,f_name,l_name):

    student = Student(first_name = f_name, last_name = l_name)
    # student = Student(first_name = 'taha', last_name = "subhani")
    student.save()
    return HttpResponse('data is inserted')

def show(request):
    students = Student.objects.all().values()
    return HttpResponse(students)

def edit(request,id):
    # student = Student.objects.get(id=id)
    student = Student.objects.get(pk=id)
    student.first_name = 'Zain'
    student.last_name = 'madni'
    student.save()
    return HttpResponse(student.first_name)

def delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()

    return HttpResponse('data is deleted')