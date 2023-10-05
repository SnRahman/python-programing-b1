from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('template/',views.tempalate),
    path('home/',views.home),
    # path('details/<id>/',views.details)
    path('details/<int:id>/',views.details),
    path('show/<name>/',views.show_name),
    path('name/',views.name),
    path('names/',views.display_list)
]