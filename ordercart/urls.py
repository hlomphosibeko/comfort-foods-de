from django.urls import path
from .views import order_cart_add, cart_detail

app_name = 'ordercart'

urlpatterns = [
    path('order-cart/add/', order_cart_add, name='order_cart_add'),
    path('', cart_detail, name='cart_detail'),
]
