from django import forms



class MenuForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

