from django import forms
from .models import CustomerComment


class CustomerCommentForm(forms.ModelForm):
    class Meta:
        model = CustomerComment
        fields = ('text',)
