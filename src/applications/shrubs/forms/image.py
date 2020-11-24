from django import forms

from applications.shrubs.models import ShrubsImage


class ShrubsImageForm(forms.ModelForm):
    original = forms.FileField(label="ShrubsImage")

    class Meta:
        model = ShrubsImage
        fields = [attr.field.name for attr in (ShrubsImage.original,)]