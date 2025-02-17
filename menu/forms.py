from django import forms
from .models import CustomerFeedback


class MenuForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ('name', 'rating', 'text')
