from django.shortcuts import render
from django.contrib import messages
from .models import About

# Create your views here.
def about_us(request):
    return render(request, "about/about.html")