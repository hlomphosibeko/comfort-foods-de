from .models import CustomerComment
from django import forms


class CustomerCommentForm(forms.ModelForm):
    """
    Shows the fields on a comment form.
    """
    class Meta:
        model = CustomerComment
        fields = ('body',)
