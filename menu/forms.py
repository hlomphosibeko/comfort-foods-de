from django import forms
from .models import CustomerFeedback

"""
class MenuForm(forms.Form):
    name = forms.CharField(required=True, error_messages={"required":"Please insert your name."})
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(label="Cooked Feedback", widget=forms.Textarea, max_length=250)

"""



class MenuForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ('name', 'rating', 'text')