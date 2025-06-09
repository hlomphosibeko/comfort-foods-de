from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CustomerCommentForm
from .models import Menu

class TestMenuViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.menu = Menu(meal_title="Menu title", customer=self.user,
                        slug="meal-title", content="Menu content", price=35,
                        category="Hearty Meals", status=0)
        self.menu.save()

    def test_render_menu_detail_page_with_customer_comment_form(self):
        response = self.client.get(reverse(
            'menu_detail', args=['meal-title']))
        self.assertEqual(response.status_code, 404)
        # self.assertIn(b"Meal title", response.content)
        # self.assertIn(b"Meal content", response.content)
        self.assertIsInstance(
            response.context['customer_comment_form'], CustomerCommentForm)
        
    def test_successful_comment_submission(self):
        """Test for writing a comment on a meal"""
        self.client.login(
            username="myUsername", password="myPassword")
        menu_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.meal(reverse(
            'menu_detail', args=['menu']), menu_data)
        self.assertEqual(response.status_code, 404)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )