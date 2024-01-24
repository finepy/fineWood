from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from django import request
from django.db.models import fields
from django.utils.text import slugify
from django import forms
# from django import request
from django.db.models import fields
from autoslug import AutoSlugField
from django_countries.widgets import CountrySelectWidget
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import Accordion, AccordionGroup
from django_select2.forms import Select2MultipleWidget
from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field, Button
from django_countries.fields import CountryField
# from django_countries.fields import CountryField
from django import forms
from .models import Customer
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,authenticate
from django_select2 import forms as s2forms


class RegForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter valid Email'}))
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Use a valid Email'}))
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
            if email and User.objects.filter(email=email).exists():
                self.add_error('email', 'This email address is already in use.')
        except ValidationError:
            raise forms.ValidationError('Enter a valid email address(e.g. Example@hello.com')
        return email
    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get('email')

    #     if email and User.objects.filter(email=email).exists():
    #         self.add_error('email', 'This email address is already in use.')

    #     return cleaned_data

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )



class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
   
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    phone = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(attrs={
            'placeholder': 'Enter valid Phone number',
            'class': 'form-control'
        }),
        
    )
    country = CountryField(blank_label='Select country').formfield(widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    # country = CountryField(blank_label="(Select country)")
    class Meta:
        model = Customer
        fields = {'profile_picture','about','country','phone'}
        # widget = {"country": CountrySelectWidget()}
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        # self.fields['country'].empty_label = "select country"
        # self.fields['username'].widget = forms.HiddenInput()




# class ProductForm(forms.ModelForm):
#     class Meta:
#         model= Product
      
#         fields = '__all__'
    
#     def __init__(self, *args, **kwargs):
#         super(ProductForm, self).__init__(*args, **kwargs)
#         # self.fields['username'].widget = forms.HiddenInput()
#         self.fields['category'].empty_label = "select category"