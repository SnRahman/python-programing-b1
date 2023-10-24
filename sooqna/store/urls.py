from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('login/',views.login_user, name='login' ),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('product-details/',views.product_detalis, name='product_details'),
    path('show-cart/',views.show_cart, name='show_cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('logout/',views.logout_user,name='logout')

]