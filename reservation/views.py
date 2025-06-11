from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse
from .models import Reservation
from django.contrib import messages
# from .forms import ReservationForm


# Create your views here.
def tableBooking(request):
    # form = ReservationForm()

    weekends = validDay(21)

    validateDates = isDateValid(weekends)

    if request.method == "POST":
        table_service = request.POST.get('table_service')
        day = request.POST.get('day')
        if table_service == None:
            messages.success(request, "Please book a table!")
            return redirect('tableBooking')

        request.session['day'] = day
        request.session['table_service'] = table_service

        return redirect('bookingSubmit')

    return render(
        request,
        "tableBooking.html",
        {
            # "form": form,
            "weekends": weekends,
            "validateDates": validateDates,
        }
    )


def bookingSubmit(request):
    customer = request.user
    times = [
        "17:00 PM", "17:30 PM", "18:00 PM", "18:30 PM", "19:00 PM", "19:30 PM",
        "20:00 PM", "20:30 PM", "21:00 PM", "21:30 PM", "22:00 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    table_service = request.session.get('table_service')

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
                                customer = customer,
                                table_service = table_service,
                                day = day,
                                time = time,
                            )
                            messages.success(request, "Reservation Saved!")
                            return redirect('userPanel')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")    
        else:
            messages.success(request, "Please Select A Table Service!")
            
    return render(request, 'bookingSubmit.html', {
        'times':hour,
    })

def userPanel(request):
    customer = request.user
    reservations = Reservation.objects.filter(customer=customer).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'customer':customer,
        'reservations':reservations,
    })

def userUpdate(request, id):
    reservation = Reservation.objects.get(pk=id)
    userdatepicked = reservation.day

    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')

    weekends = validDay(21)

    validateDates = isDateValid(weekends)

    if request.method == 'POST':
        table_service = request.POST.get('table_service')
        day = request.POST.get('day')

        request.session['day'] = day
        request.session['table_service'] = table_service

        return redirect('userUpdateSubmit', id=id)


    return render(request, 'userUpdate.html', {
            'weekends':weekends,
            'validateDates':validateDates,
            'delta24': delta24,
            'id': id,
        })

def userCancel(request, id):
    # try:
    #     reservation = Reservation.objects.get(id=id)
    #     reservation.delete()
    #     return HttpResponse("Reservation successfully canceled.")
    # except Reservation.DoesNotExist:
    #     return HttpResponse("Error: No reservation found with this ID", status=404)
    reservation = get_object_or_404(Reservation, pk=id)

    # # Date calculations
    userdatepicked = reservation.day
    today = datetime.today()
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')

    weekends = validDay(21)
    validateDates = isDateValid(weekends)

    if reservation.customer == request.user:
        reservation.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete our own bookings!')

    return redirect('userPanel')

def userUpdateSubmit(request, id):
    customer = request.user
    times = [
        "17:00 PM", "17:30 PM", "18:00 PM", "18:30 PM", "19:00 PM", "19:30 PM",
        "20:00 PM", "20:30 PM", "21:00 PM", "21:30 PM", "22:00 PM" 
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    table_service = request.session.get('table_service')
    
    hour = checkEditTime(times, day, id)
    reservation = Reservation.objects.get(pk=id)
    userSelectedTime = reservation.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekend(day)

        if table_service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if Reservation.objects.filter(day=day).count() < 11:
                        if Reservation.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            ReservationForm = Reservation.objects.filter(pk=id).update(
                                customer = customer,
                                table_service = table_service,
                                day = day,
                                time = time,
                            ) 
                            messages.success(request, "Reservation Edited, please check User Panel for confirmation!")
                            return redirect('home')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Table Service!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })

def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    
    items = Reservation.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items':items,
    })

def dayToWeekend(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validDay(days):
    
    today = datetime.now()
    weekends = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekends.append(x.strftime('%Y-%m-%d'))
    return weekends

def isDateValid(x):
    validateWeekends = []
    for j in x:
        if Reservation.objects.filter(day=j).count() < 10:
            validateWeekends.append(j)
    return validateWeekends

def checkTime(times, day):
    x = []
    for k in times:
        if Reservation.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    reservation = Reservation.objects.get(pk=id)
    time = reservation.time
    for k in times:
        if Reservation.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x