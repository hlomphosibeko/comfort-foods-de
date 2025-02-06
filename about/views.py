from django.shortcuts import render
from django.contrib import messages
from .models import About

# Create your views here.
def about_us(request):
    """
    Renders the About page.
    """
    about = About.objects.all().order_by('-updated_on').first()
    # if request.method == "POST":
    #     collaborate_form = CollaborateForm(data=request.POST)
    #     if collaborate_form.is_valid():
    #         collaborate_form.save()
    #         messages.add_message(request, messages.SUCCESS)

    # about = About.objects.all().order_by('-updated_on').first()
    # collaborate_form = CollaborateForm()

    return render(
        request, 
        "about/about.html",
        {"about": about_us,
        # "collaborate_form":collaborate_form,
        },
        )