from django import forms


class FlowerForm(forms.Form):
    quantity = forms.IntegerField()
