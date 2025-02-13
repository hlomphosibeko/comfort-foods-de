from django.urls import path
from . import views

urlpatterns = [
   path('menu/', views.menu, name='menu'),
   path('menu/<menu_category>/<menu_slug>', views.menu_page, name='menu_page')
 ]