from django.shortcuts import render

# Create your views here.
def reservations(request):
    return render(request, "reservations/reservations.html")