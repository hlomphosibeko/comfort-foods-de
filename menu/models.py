from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Not ordered"), (1, "Ordered"))

# Create your models here.
class Menu(models.Model):
    """
    Stores a single meal entry related to :model:`customer.User`
    """
    meal_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="menu_meals"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    price = models.PositiveBigIntegerField()
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The name of this meal is {self.meal_title}"


class CustomerComment(models.Model):
    """
    Stores a single comment related to :model:`customer.User`
    """
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='comments'
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.customer}"