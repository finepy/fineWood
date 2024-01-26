# Generated by Django 4.0 on 2024-01-26 21:42

import Home.filechecker
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0009_alter_product_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='Business_description',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='Business_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='friends',
        ),
        migrations.AddField(
            model_name='vendor',
            name='business_description',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='business_name',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='vendor/products/', validators=[Home.filechecker.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1.0, message='Price must be greater than or equal to 0.0')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='cover',
            field=models.ImageField(upload_to='Vendor/profile/coverPic/', validators=[Home.filechecker.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='profile_picture',
            field=models.ImageField(upload_to='Vendor/profile/profilePic/', validators=[Home.filechecker.validate_file_size]),
        ),
    ]
