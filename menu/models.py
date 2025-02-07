from django.db import models
from django.contrib.auth.models import Product, Customer
from cloudinary.models import CloudinaryField


# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    

class Orders(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    status = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=200, default='', blank=True, null=True
    )
    price = models.IntegerField(default=0)
    images = CloudinaryField('image', default='placeholder')