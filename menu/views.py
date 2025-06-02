from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Menu
from .forms import CustomerCommentForm


# Create your views here.
class MenuList(generic.ListView):
    queryset = Menu.objects.filter(status=0)
    template_name = "menu/index.html"
    paginate_by = 6


def menu_detail(request, slug):
    """
    Display an individual :model:`menu.Menu`.

    **Context**

    ``post``
        An instance of :model:`menu.Menu`.

    **Template:**

    :template:`menu/menu_detail.html`
    """

    queryset = Menu.objects.filter(status=0)
    menu = get_object_or_404(queryset, slug=slug)
    comments = menu.comments.all().order_by("-created_on")
    comment_count = menu.comments.filter(approved=True).count()
    
    if request.method == "POST":
        customer_form = CustomerCommentForm(data=request.POST)
        if customer_form.is_valid():
            comment = customer_form.save(commit=False)
            comment.customer = request.user
            comment.menu = menu
            comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment successfully submitted!'
        )

    customer_form = CustomerCommentForm()

    return render(
        request,
        "menu/menu_detail.html",
        {
            "menu": menu,
            "comments": comments,
            "comment_count": comment_count,
            "customer_form": customer_form,
        },
    )