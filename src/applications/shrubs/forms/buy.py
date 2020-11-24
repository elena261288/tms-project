from django import forms


class ShrubForm(forms.Form):
    quantity = forms.IntegerField()
