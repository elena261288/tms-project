from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin


from applications.shrubs.models import Shrubs, ShrubsImage


class ShrubsAdminForm(forms.ModelForm):
    class Meta:
        model = Shrubs
        fields = "__all__"
        widgets = {
            "shrub": forms.TextInput(),
        }


@admin.register(Shrubs)
class ShrubsAdminModel(ModelAdmin):
    form = ShrubsAdminForm


class ImageShrubsAdminForm(forms.ModelForm):
    class Meta:
        model = ShrubsImage
        fields = "__all__"
        widgets = {
            "shrubsimage": forms.ImageField,
        }


@admin.register(ShrubsImage)
class ImageShrubsAdminModel(ModelAdmin):
    form = ImageShrubsAdminForm

