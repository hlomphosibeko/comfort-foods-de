# Generated by Django 4.2.17 on 2025-02-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_customer_category_slug_menu_slug_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='menu',
            name='meal_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
