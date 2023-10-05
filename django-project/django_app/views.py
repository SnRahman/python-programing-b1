from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(requset):
    return HttpResponse('hello')

def tempalate(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home(request):
    return render(request,'home.html')

def details(request,id):
    return HttpResponse(id)

def show_name(request,name):
    return render(request,'show.html',{'name':name})

def name(request):
    return render(request,'show.html')

def display_list(request):
    names = ['Taha','Ahmad','Ahsan','Tayyab','Saad']
    return render(request,'show.html',{'names':names})