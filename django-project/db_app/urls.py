from django.urls import path
from . import views

urlpatterns = [
    path('add-student/',views.create_student,name='add_student'),
    path('register/',views.register,name='register_student'),
    path('django-form/',views.django_form,name='django-form'),

    
    path('index/',views.index),
    path('create/<f_name>/<l_name>/',views.create),
    path('show/',views.show),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete),
    # path('user-form/',views.form_view,name='submit_form')
]