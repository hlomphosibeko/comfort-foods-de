from . import views
from django.urls import path

urlpatterns = [
    path('table_booking', views.table_booking, name='table_booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit')
]