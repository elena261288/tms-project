from django import forms


class TreesForm(forms.Form):
    quantity = forms.IntegerField()
