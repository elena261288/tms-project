from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin


from applications.trees.models import Trees, TreesImage


class TreesAdminForm(forms.ModelForm):
    class Meta:
        model = Trees
        fields = "__all__"
        widgets = {
            "tree": forms.TextInput(),
        }


@admin.register(Trees)
class TreesAdminModel(ModelAdmin):
    form = TreesAdminForm


class ImageTreesAdminForm(forms.ModelForm):
    class Meta:
        model = TreesImage
        fields = "__all__"
        widgets = {
            "treesimage": forms.ImageField,
        }


@admin.register(TreesImage)
class ImageTreesAdminModel(ModelAdmin):
    form = ImageTreesAdminForm

