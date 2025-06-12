from django.test import TestCase
from .forms import CustomerCommentForm


class TestCustomerCommentForm(TestCase):
    def test_form_is_valid(self):
        customer_form = CustomerCommentForm(
            {'body': 'This is a great meal'})
        self.assertTrue(customer_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        customer_form = CustomerCommentForm({'body': ''})
        self.assertFalse(customer_form.is_valid(), msg="Form is valid")
