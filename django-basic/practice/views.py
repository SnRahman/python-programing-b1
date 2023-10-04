# Return response in views
from django.http import HttpResponse

# load html files from templates
from django.template import loader

# Create your views here.
# request parameter is for managing the url request like get or post.
def index(request):
    return HttpResponse('hello') 

def show(request):
    return HttpResponse('This is show')

def show_template(request):
    # load the actual html file and render in response
    template =  loader.get_template('show.html')
    return HttpResponse(template.render())

