from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Reservation
from django.contrib import messages


# Create your views here.
def table_booking(request):
    weekend = validDay(12)

    validateDate = isDateValid(weekend)

    if request.method == "POST":
        table_service = request.POST.get('table_service')
        day = request.POST.get('day')
        if table_service == None:
            messages.success(request, "Please book a table!")
            return redirect('table_booking')
        
        request.session['day'] = day
        request.session['table_service'] = table_service

        return redirect('bookingSubmit')
    
    return render(
        request,
        "reservation/reservation.html",
        {
            "weekend": weekend,
            "validateDate": validateDate,
        }
    )

