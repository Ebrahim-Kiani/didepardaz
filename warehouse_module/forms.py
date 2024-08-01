from django.forms import ModelForm
from .models import Brand, Mobile
from django import forms
from django_countries.widgets import CountrySelectWidget
class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']
        widgets = {
            'country': CountrySelectWidget
        }