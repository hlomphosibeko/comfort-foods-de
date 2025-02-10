from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    meal_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.CharField(
        max_length=200, default='', blank=True, null=True
    )
    price = models.PositiveIntegerField()
    images = CloudinaryField('image')




 


