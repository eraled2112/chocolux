from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from chocolux.models import Products


class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=(CKEditorUploadingWidget()))

    class Meta:
        model = Products
        fields = '__all__'


admin.site.register(Products)
admin.site.register(Application)
