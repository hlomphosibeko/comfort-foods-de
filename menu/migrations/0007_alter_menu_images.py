# Generated by Django 4.2.17 on 2025-02-10 20:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_customer_menu_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='images',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
