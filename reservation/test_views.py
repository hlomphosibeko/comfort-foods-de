from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.urls import reverse
from django.test import TestCase
from .models import Reservation

class TestReservationViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword"
        )
        self.reservation = Reservation(customer=self.user, table_service="Table Service",
                        day='2025-06-13', time="17:00 PM",
                        time_ordered='2025-06-13 17:00')
        self.reservation.save()

    def test_get_table_booking_request(self):
        response = self.client.get(reverse('tableBooking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tableBooking.html')


class TestBookingSubmitViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='myUsername',
            password='myPassword'
        )
        self.client.login(username='myUsername', password='myPassword')
        self.session = self.client.session
        self.session["day"] = (datetime.now() + timedelta(days=21)).strftime('%Y-%m-%d')
        self.session["table_service"] = "Table for 2"
        self.session.save()

    def test_get_booking_submission_request(self):
        response = self.client.get(reverse('bookingSubmit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingSubmit.html')

    def test_post_request_valid_booking(self):
        response = self.client.post(reverse("bookingSubmit"), {"time": "20:00 PM"})
        self.assertEqual(response.status_code, 200)
        

    def test_post_request_time_already_reserved(self):
        Reservation.objects.create(
            customer=self.user, table_service="Table for 2", day=self.session["day"], time="19:00 PM"
        )
        response = self.client.post(reverse("bookingSubmit"), {"time": "19:00 PM"})
        self.assertEqual(response.status_code, 200)