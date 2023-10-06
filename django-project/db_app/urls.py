from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    # path('add_student/',views.create_student),
    # path('register/',views.register),
    path('create/<f_name>/<l_name>/',views.create),
    path('show/',views.show),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete)
]