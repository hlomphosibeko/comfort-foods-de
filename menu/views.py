from django.shortcuts import render
from .models import Menu

# Create your views here.
def menu(request):
    my_menu = Menu.objects.all()
    return render(request, "menu/menu.html",{
        'my_menu': my_menu})
