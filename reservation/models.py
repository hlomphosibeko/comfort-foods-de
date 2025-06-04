from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

TABLE_SERVICE = (
    ("Table for 2", "Table for 2"),
    ("Table for 4", "Table for 4"),
    ("Table for 6", "Table for 6"),
    ("Table for 10", "Table for 10"),
    ("Table for 12", "Table for 12"),
)

BOOKING_TIMES = (
    ("17:OO PM", "17:00 PM"),
    ("17:3O PM", "17:30 PM"),
    ("18:OO PM", "18:00 PM"),
    ("18:3O PM", "18:30 PM"),
    ("19:OO PM", "19:OO PM"),
    ("19:3O PM", "19:3O PM"),
    ("20:OO PM", "20:00 PM"),
    ("20:3O PM", "20:30 PM"),
    ("21:OO PM", "21:00 PM"),
    ("21:3O PM", "21:30 PM"),
    ("22:OO PM", "22:OO PM"),
)


class Reservation(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    table_service = models.CharField(
        max_length=50, choices=TABLE_SERVICE, default="Table for 2"
    )
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=BOOKING_TIMES, default="17:00 PM"
    )

    def __str__(self):
        return f"{self.customer.username} | day: {self.day} | time: {self.time}"
