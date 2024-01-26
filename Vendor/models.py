from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.utils.html import format_html
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from colorfield.fields import ColorField
from Home.filechecker import validate_file_size
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator


class NonNumericValidator(RegexValidator):
    regex = r'^[^0-9]*$'
    message = 'Numeric characters are not allowed.'
# Create your models here.

class Vendor(models.Model):
   
   
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture =  models.ImageField(upload_to='Vendor/profile/profilePic/',validators=[validate_file_size])
    cover=  models.ImageField(upload_to='Vendor/profile/coverPic/',validators=[validate_file_size])
    business_name = models.CharField(max_length=50)

    # friends = models.ManyToManyField(User, related_name='user_friends')
    business_description = models.CharField(max_length=255)
    phone = PhoneNumberField()
    # follower = models.ManyToManyField(User, related_name='vendor_followers', blank=True)
    country = CountryField()
    # friends = models.ManyToManyField(User, related_name='user_friends')
    # last_activity = models.DateTimeField(null=True, blank=True)
    # friend_requests = models.ManyToManyField(User,  related_name='received_friend_requests')
    # state = models.ForeignKey(Location,on_delete=models.CASCADE)
  
    def __str__(self) -> str:
        return f'{self.username}'

class Category(models.Model):

    name = models.CharField(max_length = 25)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    def __str__(self):
        return str(self.name)
    # def get_absolut_url(self):
    #     return reverse('Myapp:category_filter', args={self.slug})
    
class Product(models.Model):
    vendor =  models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=25) 
    image = models.ImageField(upload_to='vendor/products/',validators=[validate_file_size]) 
    description = models.CharField(max_length=255)
    # color = ColorField(default = "#FF0000", format="hexa")
    color = models.CharField(max_length = 25)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    price = models.FloatField(validators=[MinValueValidator(1.0, message="Price must be greater than or equal to 0.0")])
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return f" {self.vendor.usernam} {self.name}"
    
  
    


class Feedback(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    feedback  = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
    rating = models.PositiveSmallIntegerField(choices=(
        (1, "⭐☆☆☆☆"),
        (2, "⭐⭐☆☆☆"),
        (3, "⭐⭐⭐☆☆"),
        (4, "⭐⭐⭐⭐☆"),
        (5, "⭐⭐⭐⭐⭐"),
    ))

class Wallet(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.00)



# class Order(models.Model):
#     product = models.ForeignKey(Product,
#                                 on_delete=models.CASCADE)
#     customer = models.ForeignKey(User,
#                                  on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.IntegerField()
#     address = models.CharField (max_length=50)
#     image = models.ImageField(upload_to='proof/', blank=True, default="/proof/succ.jpg")
#     phone = models.CharField (max_length=50)
#     date = models.DateTimeField (auto_now=True)
    
#     status = models.BooleanField (default=False)

#     def placeOrder(self):
#         self.save()

#     @staticmethod
#     def get_orders_by_customer(customer_id):
#         return Order.objects.filter(customer=customer_id).order_by('-date')
    
#     def __str__(self):
#         return str(self.product.name)
    

# # class Orders(models.Model):
# #     product = models.ForeignKey(Product,
# #                                 on_delete=models.CASCADE)
# #     customer = models.ForeignKey(User,
# #                                  on_delete=models.CASCADE)
# #     quantity = models.IntegerField(default=1)
# #     price = models.IntegerField()
# #     address = models.CharField (max_length=50)
# #     image = models.ImageField(upload_to='proof/' ,null = True, blank= True )
# #     phone = models.CharField (max_length=50)
# #     date = models.DateTimeField (auto_now=True)
    
# #     status = models.BooleanField (default=False)

# #     def placeOrder(self):
# #         self.save()

# #     @staticmethod
# #     def get_orders_by_customer(customer_id):
# #         return Order.objects.filter(customer=customer_id).order_by('-date')
    
# #     def __str__(self):
# #         return str(self.product.name)
    
# #     def img_preview(self): 
# #         return mark_safe('<img src="/directory/%s" width="150" height="150" />' % {self.image.url})

# #     img_preview.short_description = 'Image'



# class Payment(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE,)
#     amount = models.FloatField()
#     ref = models.CharField(max_length=200)
#     address = models.CharField (max_length=50)
#     image = models.ImageField(upload_to='proof/', default='/proof/succ.jpg' )
#     phone = models.CharField (max_length=50)
#     email = models.EmailField()
#     verified = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-date_created',)

#     def __str__(self):
#         return f"Payment: {self.amount}"

#     def save(self, *args, **kwargs):
#         while not self.ref:
#             ref = secrets.token_urlsafe(50)
#             object_with_similar_ref = Payment.objects.filter(ref=ref)
#             if not object_with_similar_ref:
#                 self.ref = ref

#         super().save(*args, **kwargs)
#     def amount_value(self):
#         return int(self.amount) * 100
#     def verify_payment(self):
#         paystack = Paystack()
#         status, result = paystack.verify_payment(self.ref, self.amount)
#         if status:
#             if result['amount'] / 100 == self.amount:
#                 self.verified = True
#             self.save()
#         if self.verified:
#             return True
#         return False