# Generated by Django 4.2.17 on 2025-05-29 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_meal_title_menu_menu_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_title',
            new_name='meal_title',
        ),
    ]
