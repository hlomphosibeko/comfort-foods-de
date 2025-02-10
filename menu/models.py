from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    meal_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    category = models.CharField(max_length=250)
    description = models.CharField(
        max_length=200, default='', blank=True, null=True
    )
    price = models.PositiveIntegerField()
    images = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.meal_name


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
 


