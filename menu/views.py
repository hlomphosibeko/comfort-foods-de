from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Menu, Category, Order, CustomerFeedback
from django.contrib import messages
from .forms import MenuForm

# Create your views here.
def menu(request):
    my_menu = Menu.objects.all()
    platters = Menu.objects.filter(category__name = 'Braai Platters')
    hearty_meals = Menu.objects.filter(category__name = 'Hearty Meals')
    my_sides = Menu.objects.filter(category__name = 'Sides')
    drinks = Menu.objects.filter(category__name = 'Mzansi Drinks')
    return render(request, "menu/menu.html",{
        'my_menu': my_menu,
        'platters': platters,
        'hearty_meals': hearty_meals,
        'my_sides': my_sides,
        'drinks': drinks})


def category(request):
    my_category = Category.objects.order_by(Category.name).all()
    return render(request, "menu/menu.html", {
        'my_category': my_category})


def menu_detail(request, slug):
    my_details = Menu.objects.get(slug=slug)
    form = MenuForm()
    reviews = CustomerFeedback.objects.filter(menu=my_details)
    if request.method == "GET":
        
        return render(request, "menu/menu_detail.html",
        {"my_details": my_details,
         "form": form,
         "reviews": reviews})
    else:
        form = MenuForm(request.POST)
        if form.is_valid():
            feedback = CustomerFeedback(
                name = form.cleaned_data["name"],
                rating = form.cleaned_data["rating"],
                menu = my_details,
                text = form.cleaned_data["text"]
            )
            feedback.save
            messages.success(request, "Your cooked thoughts were successfully submitted ☺!")

        return render(request, "menu/menu_detail.html",
        {"my_details": my_details,
         "form": form,
         "reviews": reviews})
    




def menu_order_delete(request):
    if request.method == 'POST':
        order = get_object_or_404(Order)
        order.delete()
        return HttpResponseRedirect()
