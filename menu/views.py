from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Menu


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

    queryset = Menu.objects.filter(status=1)
    menu = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "menu/menu_detail.html",
        {"menu": menu},
    )