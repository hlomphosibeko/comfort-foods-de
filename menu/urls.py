from django.urls import path
from . import views

urlpatterns = [
   path('menu/', views.menu, name='menu'),
   path('<slug:slug>/', views.menu_detail, name='menu_detail'),
 ]