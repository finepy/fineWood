# Generated by Django 4.0 on 2024-01-23 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=15)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0.0)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='App/social/profilePic/')),
                ('cover', models.ImageField(upload_to='App/social/coverPic/')),
                ('about', models.CharField(max_length=1000)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('friends', models.ManyToManyField(related_name='user_friends', to=settings.AUTH_USER_MODEL)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.category')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '⭐☆☆☆☆'), (2, '⭐⭐☆☆☆'), (3, '⭐⭐⭐☆☆'), (4, '⭐⭐⭐⭐☆'), (5, '⭐⭐⭐⭐⭐')])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
