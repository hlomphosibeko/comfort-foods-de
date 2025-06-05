from django import forms


class ReservationForm(forms.Form):
    TABLE_SERVICE = [
        ("1", "Table for 2"),
        ("2", "Table for 4"),
        ("3", "Table for 6"),
        ("4", "Table for 10"),
        ("5", "Table for 12"),
    ]
    table = forms.ChoiceField(choices=TABLE_SERVICE, widget=forms.Select)
    
