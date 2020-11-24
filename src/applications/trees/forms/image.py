from django import forms

from applications.shrubs.models import TreesImage


class TreesImageForm(forms.ModelForm):
    original = forms.FileField(label="TreesImage")

    class Meta:
        model = TreesImage
        fields = [attr.field.name for attr in (TreesImage.original,)]