from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def say_hello(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    # return HttpResponse('Hello world!')
