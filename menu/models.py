from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Menu(models.Model):
    meal_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(
        Category, related_name='menu', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    images = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.meal_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Order(models.Model):
    meal = models.ForeignKey(
        Menu, on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status


class CustomerFeedback(models.Model):
    name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.menu} | Rating {self.rating}"
