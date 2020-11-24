from django import forms

from applications.flowers.models import FlowersImage


class FlowersImageForm(forms.ModelForm):
    original = forms.FileField(label="FlowersImage")

    class Meta:
        model = FlowersImage
        fields = [attr.field.name for attr in (FlowersImage.original,)]