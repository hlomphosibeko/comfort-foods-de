from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Menu, CustomerFeedback
from .forms import MenuForm


class MenuList(generic.ListView):
    queryset = Menu.objects.all()
    template_name = "menu/menu.html"


def menu_detail(request, slug):
    """
    Display an individual :model:`menu.Menu`.

    **Context**

    ``post``
        An instance of :model:`menu.Menu`.

    **Template:**

    :template:`menu/menu_detail.html`
    """
    queryset = Menu.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    customer_comments = meal.comments.all().order_by("-created_on")

    if request.method == "POST":
        customer_form = MenuForm(data=request.POST)
        if customer_form.is_valid():
            comment = customer_form.save(commit=False)
            comment.customer = request.user
            comment.meal = meal
            comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted!'
        )

    customer_form = MenuForm()

    return render(
        request,
        "menu/menu_detail.html",
        {
            "meal": meal,
            "customer_comments": customer_comments,
            "customer_form": customer_form,
        },
    )


def customer_comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Menu.objects.all()
        meal = get_object_or_404(queryset, slug=slug)
        customer_comments = get_object_or_404(CustomerFeedback, pk=comment_id)
        customer_form = MenuForm(
            data=request.POST, instance=customer_comments)

        if customer_form.is_valid() and customer_comments.customer == request.user:
            comment = customer_form.save(commit=False)
            comment.meal = meal
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))


def customer_comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Menu.objects.all()
    meal = get_object_or_404(queryset, slug=slug)
    customer_comments = get_object_or_404(CustomerFeedback, pk=comment_id)

    if customer_comments.customer == request.user:
        customer_comments.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))


def order_details(request, slug, ):
    """
    view customer order
    """
    queryset = Menu.objects.all()

# def menu(request):
#     my_menu = Menu.objects.all()
#     platters = Menu.objects.filter(category__name = 'Braai Platters')
#     hearty_meals = Menu.objects.filter(category__name = 'Hearty Meals')
#     my_sides = Menu.objects.filter(category__name = 'Sides')
#     drinks = Menu.objects.filter(category__name = 'Mzansi Drinks')
#     #menu_id=Menu.Id
#     return render(request, "menu/menu.html",{
#         'my_menu': my_menu,
#         'platters': platters,
#         'hearty_meals': hearty_meals,
#         'my_sides': my_sides,
#         'drinks': drinks
#         #'menu_id':menu_id
#         })

# # def signup(request):
# #     return render(request, )


# def category(request):
#     my_category = Category.objects.order_by(Category.name).all()
#     return render(request, "menu/menu.html", {
#         'my_category': my_category})


# 


# def edit_feedback(request, slug, menu_id):
#     """
#     view to edit comments
#     """
#     if request.method == "POST":
#        my_details =  get_object_or_404(slug=slug)
#        my_feedback = get_object_or_404(CustomerFeedback, pk=menu_id)
#        form = MenuForm(data=request.POST, instance=my_feedback)

#        if form.is_valid() and my_feedback.menu == request.my_details:
#            new_feedback = form.save(commit=False)
#            new_feedback.my_details = my_details
#            new_feedback.approve = False
#            new_feedback.save()
#            messages.add_message(request, messages.SUCCESS, "Feedback Updated!")
#     else:
#            messages.add_message(
#                request, messages.ERROR, "Error updating feedback!")
    
#     return HttpResponseRedirect(reverse('my_details', args=[slug]))

    
# def delete_feedback(request, slug,def menu_detail(request, slug):
#     my_details = Menu.objects.get(slug=slug)
#     my_feedback = CustomerFeedback.objects.filter(menu=my_details).first()
#     form = MenuForm(instance=my_feedback)
#     reviews = CustomerFeedback.objects.filter(menu=my_details)
    
#     if request.method == "GET":
#         return render(request, "menu/menu_detail.html", {
#             "my_details": my_details,
#             "form": form,
#             "reviews": reviews,
#         })
#     else:
#         form = MenuForm(request.POST,instance=my_feedback)
#         if form.is_valid():
#             new_feedback = form.save(commit=False)
#             new_feedback.menu = my_details
#             new_feedback.save()
#             messages.success(request, "Your cooked thoughts were successfully submitted ☺!")

#         # form = MenuForm()

#         return render(request, "menu/menu_detail.html", {
#             "my_details": my_details,
#             "form": form,
#             "reviews": reviews,
#         }) menu_id):


# def menu_order_delete(request):
#     if request.method == 'POST':
#         order = get_object_or_404(Order)
#         order.delete()
#         return HttpResponseRedirect()
