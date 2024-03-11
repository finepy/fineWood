from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.models import EmailAddress

class Customer(models.Model):

    class SexChoices(models.TextChoices):
        Male = "Male"
        Female = "Female"

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='Customer/profile/profilePic/'
    )
    about = models.CharField(max_length=1000)
    phone = PhoneNumberField()
    country = CountryField()
    gender = models.CharField(max_length=10, choices=SexChoices.choices)

    def __str__(self) -> str:
        return f'{self.username}'

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customer.save()

@receiver(post_save, sender=User)
def create_email_address(sender, instance, created, **kwargs):
    if created:
        EmailAddress.objects.create(user=instance, email=instance.email, verified=False)
