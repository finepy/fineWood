from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('started/', views.started, name='started'),
    path('shop/', views.shop, name='shop'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('cart', views.cart, name='cart'),
    # path('productupload/', views.productupload, name='productupload'),

]


urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 