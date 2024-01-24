from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from Vendor.models import Category, Product
from Customer.forms import RegForm, UpdateProfileForm
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from Vendor.models import Vendor, Category
from .models import Customer
import os
from cart.cart import Cart
# Create your views here.

def index(request):
    return render(request, 'index.html')

class ProfileView(SessionWizardView):
    
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profile/profilePic/'))
    # form_list = [RegForm,PictureUpdate,UpdateProfileForm] for as many as possible steps 
    form_list = [RegForm,UpdateProfileForm]
    template_name = 'Customer/registration.html'
    # Do something with the cleaned_data, then redirect
    # to a "success" page.
    def done(self, form_list, **kwargs):

        
        
        user_form = form_list[0]
        username = user_form.cleaned_data.get('username')
        
        print(username)
        if form_list:
            user_form.save()
            userr = User.objects.get(username__icontains=username)
            profile = form_list[1].save(commit=False)
            # inactive_user = send_verification_email(self.request, user_form)
        
            profile.username =  userr
            profile.save()
        

            messages.info(self.request, " account created successfully ")
            return redirect('/login')
        
        else:
            print("something is wrong ")
            
        return redirect('/index')
    





# def login(request):

#     if request.user.is_authenticated:
#         return redirect('Vendor:index')
     
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username =username, password = password)
#         profile = Vendor.objects.filter(username=user)
#         if profile:
#             messages.info(request, f'{user.username} you registered as a vendor not a customer ')
#             return redirect('/Vendor/login/')
 
#         elif user is not None:
#             auth.login(request,user)
#             return redirect('Customer:index')
#         else:
#             messages.error(request, 'invalid login details')
#             form = AuthenticationForm()
#             return render(request,'Customer/login.html',{'form':form})
     
#     else:
#         form = AuthenticationForm()
#         return render(request, 'Customer/login.html', {'form':form})



def shop(request):
    return render(request, 'shop.html')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    kent = product.name
    cart.add(product=product)
    messages.success(request, f"{product.name} added successfully ")
    print(cart)
    return redirect(request.META.get('HTTP_REFERER'))



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/cart-detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/Customer/cart-detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
        return redirect("/Customer/cart-detail")
    except:
        messages.error(request,"not possible agba hacker")
        return redirect("/Customer/cart-detail")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/Customer/cart-detail")

def cart_detail(request):
    return render(request, 'Customer/cart.html')




def delete(request, product_id):
    c = request.session.get('cart',[product_id]==product_id)
    c.pop(product_id)
    request.session.modified = True

    return redirect('cart-detail')

# def logout(request):
#     auth.logout(request)
#     messages.info(request, 'Come back soon')
#     return redirect('/Customer/login/')