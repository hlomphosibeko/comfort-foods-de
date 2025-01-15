from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_foody(request):
    return HttpResponse("Hello foodies, Welcome to Comfort Foods Cuisine Germany!")