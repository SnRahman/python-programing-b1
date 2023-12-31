from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms.users_form import StudentForm
from .models import Student

# Create your views here.

def users(request):
    students = Student.objects.all()
    return render(request,'users.html',{'students':students})

def create(request):
    if request.method == 'GET':
        form = StudentForm()
        return render(request,'form.html',{'form':form})
    else:
        form = StudentForm(request.POST,request.FILES)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            image = form.cleaned_data['file']
            student = Student(first_name = first_name, last_name= last_name, email=email, image = image)
            student.save()
            return redirect('users')
        else:
            # return HttpResponse('errors')
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {form.fields[field_name].label}: {error}")

            return redirect('create')


def update(request,id):
    # student = Student.objects.get(pk=id)

    instance = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('users')
    return render(request, 'update-form.html', {'form': form}) 


    # if request.method =='GET':
    #     form = StudentForm()
    #     # student = Student.objects.get(id=id)
    #     return render(request,'update-form.html',{'form':form,'student':student})
    # else:
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     email = request.POST.get('email')

    #     student.first_name = first_name
    #     student.last_name = last_name
    #     student.email = email
    #     student.save()
    #     return redirect('users')

def delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('users')

    