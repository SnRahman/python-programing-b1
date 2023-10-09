from django.urls import path
from . import views

urlpatterns = [
    path('get-users/',views.users, name='users'),
    path('create/',views.create,name='create'),
    path('update-user/<int:id>/',views.update, name='update'),
    path('delete-student/<int:id>/',views.delete, name='delete')

]
