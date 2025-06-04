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

def bookingSubmit(request):
    customer = request.user
    times = [
        "17:OO PM", "17:3O PM", "18:OO PM", "18:3O PM", "19:OO PM", "19:3O PM", "20:OO PM", "20:3O PM", "21:OO PM", "21:3O PM", "22:OO PM",  
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    tabele_service = request.session.get('table_service')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekend(day)

        if table_service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if Reservation.objects.filter(day=day).count() < 11:
                        if Reservation.objects.filter(day=day, time=time).count() < 1:
                            ReservationForm = Reservation.objects.get_or_create(
                                customer = user,
                                table_service = table_service,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "Reservation Saved!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                            messages.success(request, "The Selected Day Is Full!")
                else:
                        messages.success(request, "The Selected Date Is Incorrect")
            else:
                        messages.success(request, "The Selected Date Isn't In The Correct Time Period!")    
        else:
                messages.success(request, "Please Select A Service!")
                return redirect('userPanel')
    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })