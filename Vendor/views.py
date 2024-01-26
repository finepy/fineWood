from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Category, Product
from .forms import RegForm, UpdateProfileForm, ProductForm
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Vendor, Category,Wallet
from Customer.models import Customer
import os
# Create your views here.

def index(request):
    return render(request, 'index.html')

class ProfileView(SessionWizardView):
    
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profile/profilePic/'))
    # form_list = [RegForm,PictureUpdate,UpdateProfileForm] for as many as possible steps 
    form_list = [RegForm,UpdateProfileForm]
    template_name = 'Vendor/registration.html'
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
            Wallet.objects.create(vendor=userr)
        
        

            messages.info(self.request, " account and wallet created successfully ")
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
#         profile = Customer.objects.filter(username=user)
#         if profile:
#             messages.info(request, f'{user.username} you registered as a customer not vendor ')
#             return redirect('/Customer/login/')
 
#         elif user is not None:
#             auth.login(request,user)
#             return redirect('Vendor:index')
#         else:
#             messages.error(request, 'invalid login details')
#             form = AuthenticationForm()
#             return render(request,'Vendor/login.html',{'form':form})
     
#     else:
#         form = AuthenticationForm()
#         return render(request, 'Vendor/login.html', {'form':form})



def shop(request):
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')

def productupload(request):
    if request.user.is_active and request.user.is_authenticated:
        user= get_object_or_404(Vendor, username=request.user)
        customer = Customer.objects.filter(username=request.user)
        vendor = Vendor.objects.filter(username=request.user)
        # user = Vendor.objects.filter(username=request.user)
        if user:
    

            if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)
                
                if form.is_valid():
                    messages.success(request, 'product added successfully')
                    form.save()
                
                
                    return redirect(request.META.get('HTTP_REFERER'))
                else:
                    messages.success(request, 'product not added ')
                    return redirect(request.META.get('HTTP_REFERER'))

            else:
                form = ProductForm(initial = {'vendor':user})
            
            return render(request, 'Vendor/productupload.html', {'form': form,'customer':customer,'vendor':vendor})
        else:
            messages.info(request, "You are not a vendor ")
            return redirect('/index')
    else:
        messages.info(request, "You are not authorized ")
        return redirect('/login')

    
    

# def create(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
# #       {{content|safe }}
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#             # name = request.POST.get('name')
#             # body = request.POST.get('description')
#             # if Product.objects.filter(name=name):
#             #     messages.error(request, 'Blog already exist')
#             #     return redirect('create')
#             # elif len(body)  < 255:
#             #     messages.error(request, 'your content is too small ')
#             #     return redirect('create')
#             # else:
#             #     form.save()
#             #     return redirect('home')
         
#         else:
#             messages.error(request, 'something went wrong')
#             return redirect('create')
    
    
#     else:
#         form = ProductForm(initial = {'vendor':request.user.id,'title':request.user.username})
#         return render(request,'uploader.html',{'form':form})