from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms.MyForm import StudentForm

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


def create_student(request):
    return render(request,'form.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')

        if first_name and last_name and email:
            
            student = Student(first_name = first_name, last_name=last_name,email=email)
            student.save()

            return HttpResponse('form is submited')
        else:
            return HttpResponse('Enter The valid inputs') 
    else:
        return HttpResponse('Method not allowed')


def django_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            email = form.cleaned_data['email']
            student = Student(first_name = f_name, last_name=l_name,email=email)
            student.save()
        return HttpResponse('form is submitted')
    else:
        form = StudentForm()
        return render(request,'django-form.html',{'form':form})
