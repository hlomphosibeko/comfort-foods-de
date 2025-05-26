from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Menu(models.Model):
    meal_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_menus'
    )
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    images = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.meal_name


class CustomerFeedback(models.Model):
    meal = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='comments'
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=False)
    text = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment {self.text} by {self.customer}"


# class (models.Model):
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     email = models.EmailField()

#     def __str__(self):
#         return self.first_name


# class Order(models.Model):
#     meal = models.ForeignKey(
#         Menu, on_delete=models.CASCADE
#     )
#     customer = models.ForeignKey(
#         Customer, on_delete=models.CASCADE
#     )
#     status = models.CharField(max_length=200)

#     def __str__(self):
#         return self.status



