# Generated by Django 4.2.17 on 2025-02-12 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_alter_menu_category_alter_menu_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
