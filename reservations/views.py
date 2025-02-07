from django.shortcuts import render
from .models import Reservation

# Create your views here.
def reservations(request):
    my_reserves = Reservation.objects.all().order_by('-date_of_reserv')
    return render(request, "reservations/reservations.html",
                  {'my_reserves': my_reserves})