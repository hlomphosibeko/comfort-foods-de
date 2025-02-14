from django import forms



class MenuForm(forms.Form):
    name = forms.CharField(required=True, error_messages={"required":"Please insert your name."})
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(label="Cooked Feedback", widget=forms.Textarea, max_length=250)

