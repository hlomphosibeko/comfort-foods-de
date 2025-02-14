from django.urls import path
from . import views

urlpatterns = [
   path('menu/', views.menu, name='menu'),
  #  path('signup')
  # path('category')
   path('<slug:slug>/', views.menu_detail, name='menu_detail'),
 ]