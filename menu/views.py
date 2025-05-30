from django.shortcuts import render
from django.views import generic
from .models import Menu


# Create your views here.
class MenuList(generic.ListView):
    queryset = Menu.objects.filter(status=0)
    template_name = "menu/index.html"
    paginate_by = 6
