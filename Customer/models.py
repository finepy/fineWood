from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Customer(models.Model):
   
   
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =  models.ImageField(upload_to='Customer/profile/profilePic/')

    about = models.CharField(max_length=1000)
    phone = PhoneNumberField()
    # follower = models.ManyToManyField(User, related_name='customer_followers', blank=True)
    country = CountryField()
    
   
  
    def __str__(self) -> str:
        return f'{self.username}'