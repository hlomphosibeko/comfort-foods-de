from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Not ordered"), (1, "Ordered"))

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Menu(models.Model):
    meal_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="menu_meals"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category'
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    price = models.PositiveBigIntegerField()
