from django.shortcuts import render, get_object_or_404, reverse
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
    #menu_id=Menu.Id
    return render(request, "menu/menu.html",{
        'my_menu': my_menu,
        'platters': platters,
        'hearty_meals': hearty_meals,
        'my_sides': my_sides,
        'drinks': drinks
        #'menu_id':menu_id
        })

# def signup(request):
#     return render(request, )


def category(request):
    my_category = Category.objects.order_by(Category.name).all()
    return render(request, "menu/menu.html", {
        'my_category': my_category})


def menu_detail(request, slug):
    my_details = Menu.objects.get(slug=slug)
    my_feedback = CustomerFeedback.objects.filter(menu=my_details).first()
    form = MenuForm(instance=my_feedback)
    reviews = CustomerFeedback.objects.filter(menu=my_details)
    
    if request.method == "GET":
        
        return render(request, "menu/menu_detail.html", {
            "my_details": my_details,
            "form": form,
            "reviews": reviews,
        })
    else:
        form = MenuForm(request.POST,instance=my_feedback)
        if form.is_valid():
            new_feedback = form.save(commit=False)
            new_feedback.menu = my_details
            new_feedback.save()
            messages.success(request, "Your cooked thoughts were successfully submitted ☺!")

        # form = MenuForm()

        return render(request, "menu/menu_detail.html", {
            "my_details": my_details,
            "form": form,
            "reviews": reviews,
            
        })


def edit_feedback(request, slug, menu_id):
    """
    view to edit comments
    """
    if request.method == "POST":
       my_details =  get_object_or_404(slug=slug)
       my_feedback = get_object_or_404(CustomerFeedback, pk=menu_id)
       form = MenuForm(data=request.POST, instance=my_feedback)

       if form.is_valid() and my_feedback.menu == request.my_details:
           new_feedback = form.save(commit=False)
           new_feedback.my_details = my_details
           new_feedback.approve = False
           new_feedback.save()
           messages.add_message(request, messages.SUCCESS, "Feedback Updated!")
    else:
           messages.add_message(request, messages.ERROR, "Error updating feedback!")
    
    return HttpResponseRedirect(reverse('my_details', args=[slug]))

    
# def delete_feedback(request, slug, menu_id):


def menu_order_delete(request):
    if request.method == 'POST':
        order = get_object_or_404(Order)
        order.delete()
        return HttpResponseRedirect()



