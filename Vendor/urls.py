from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Vendor'
urlpatterns = [
    path('', views.index, name='index'),
    # path('shop', views.shop, name='shop'),
    # path('cart', views.cart, name='cart'),
    path('productupload/', views.productupload, name='productupload'),
    path('register/', views.ProfileView.as_view(), name="register"),
    # path('login/',views.login, name='login'),
    # path('logout/', views.logout, name='logout'),

]