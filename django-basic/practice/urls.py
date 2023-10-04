from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index ),
    path('show/',views.show),
    path('template/',views.show_template)

]
