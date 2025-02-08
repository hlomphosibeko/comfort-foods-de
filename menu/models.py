from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Menu(models.Model):
    meal_name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=200, default='', blank=True, null=True
    )
    price = models.IntegerField(default=0)
    images = CloudinaryField('image', default='placeholder')  

    def __str__(self):
        return self.meal_name 

class Orders(models.Model):
    meal = models.ForeignKey(
        Menu, on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status


