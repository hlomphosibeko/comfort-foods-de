from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Menu, Category, Order

# Create your views here.
def menu(request):
    my_menu = Menu.objects.all()
    platters = Menu.objects.filter(category__name = 'Braai Platters')
    hearty_meals = Menu.objects.filter(category__name = 'Hearty Meals')
    my_sides = Menu.objects.filter(category__name = 'Sides')
    drinks = Menu.objects.filter(category__name = 'Mzansi Drinks')
    # my_platter = platters.objects.filter(category__name = '')
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
    my_details = get_object_or_404(slug=slug)
    return render(request, "menu/menu_detail.html",
                  {"my_details": my_details})




def menu_order_delete(request):
    if request.method == 'POST':
        order = get_object_or_404(Order)
        order.delete()
        return HttpResponseRedirect()
