from django import forms



class MenuForm(forms.Form):
    name = forms.CharField(required=True, error_messages={"required":"Please insert your name."})
    

