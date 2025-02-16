from django.urls import path
from . import views

urlpatterns = [
   path('menu/', views.menu, name='menu'),
  #  path('signup')
  # path('category')
   path('<slug:slug>/', views.menu_detail, name='menu_detail'),
   path('<slug:slug>/edit_feedback/<int:menu_id>', views.edit_feedback, name='edit_feedback'),
 ]

