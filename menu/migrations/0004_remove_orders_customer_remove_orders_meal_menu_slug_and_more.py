# Generated by Django 4.2.17 on 2025-02-10 19:10

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_meal_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='meal',
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(default='exit', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='images',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='meal_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
