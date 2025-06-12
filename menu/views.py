from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Menu, CustomerComment
from .forms import CustomerCommentForm


# Create your views here.
class MenuList(generic.ListView):
    queryset = Menu.objects.all()
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
                'Comment successfully submitted and awaiting approval!'
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


def customer_comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Menu.objects.filter(status=0)
        menu = get_object_or_404(queryset, slug=slug)
        customer_comment = get_object_or_404(CustomerComment, pk=comment_id)
        customer_form = CustomerCommentForm(
            data=request.POST, instance=customer_comment)

        if customer_form.is_valid() and customer_comment.customer == request.user:
            comment = customer_form.save(commit=False)
            comment.menu = menu
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment successfully Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))


def customer_comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Menu.objects.all()
    menu = get_object_or_404(queryset, slug=slug)
    customer_comment = get_object_or_404(CustomerComment, pk=comment_id)

    if customer_comment.customer == request.user:
        customer_comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('menu_detail', args=[slug]))
