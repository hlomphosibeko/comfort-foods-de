from django.db import models

# Create your models here.
class Reservation(models.Model):
    people_booked = models.IntegerField()
    date_of_reserv = models.DateTimeField()
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    preference = models.TextField(blank=True)

    
    def __str__(self):
        return self.full_name