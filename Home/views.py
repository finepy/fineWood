from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
# from .forms import ProductForm
from Vendor.models import Category, Product, Vendor
from Customer.models import Customer

# Create your views here.

def index(request):
   

    if request.user.is_authenticated:
        customer = Customer.objects.filter(username=request.user).first()
        vendor = Vendor.objects.filter(username=request.user).first()

        return render(request, 'index.html', {'customer': customer, 'vendor': vendor})
    else:
        return render(request, 'index.html')


def started(request):
    return render(request, 'started.html')

def cart(request):
    return render(request, 'cart.html')

def shop(request):
    product = Product.objects.all()
    
    customer = Customer.objects.filter(username=request.user).exists
    vendor = Vendor.objects.filter(username=request.user).exists
    return render(request, 'shop.html', {'customer':customer,'vendor':vendor,'product':product})

# def productupload(request):

#     if request.user.is_superuser:
   

#         if request.method == 'POST':
#             form = ProductForm(request.POST, request.FILES)
            
#             if form.is_valid():
#                 messages.success(request, 'product added successfully')
#                 form.save()
            
            
#                 return redirect('/product/')
#             else:
#                 print("something went wrong")
#         else:
#             form = ProductForm()
        
#         return render(request, 'productupload.html', {'form': form})
#     else:
#         messages.info(request, "You are not authorized ")
#         return redirect('index')
    
def login(request):

    if request.user.is_authenticated:
        return redirect('index')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        
 
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'invalid login details')
            form = AuthenticationForm()
            return render(request,'login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
# def logout(request):
#     auth.logout(request)
#     messages.info(request, 'Come back soon')
#     return redirect('/login/')
def logout(request):
    request.session.clear()
    return redirect('/login/')