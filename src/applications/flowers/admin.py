from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin


from applications.flowers.models import Flowers, FlowersImage


class FlowersAdminForm(forms.ModelForm):
    class Meta:
        model = Flowers
        fields = "__all__"
        widgets = {
            "flower": forms.TextInput(),
        }


@admin.register(Flowers)
class FlowersAdminModel(ModelAdmin):
    form = FlowersAdminForm


class ImageFlowersAdminForm(forms.ModelForm):
    class Meta:
        model = FlowersImage
        fields = "__all__"
        widgets = {
            "flowersimage": forms.ImageField,
        }


@admin.register(FlowersImage)
class ImageFlowersAdminModel(ModelAdmin):
    form = ImageFlowersAdminForm

