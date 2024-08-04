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


class MobileForm(ModelForm):
    TWO_CHOICES = (
        (True, 'Yes'),
        (False, "No")
    )

    is_available = forms.TypedChoiceField(
        choices=TWO_CHOICES,
        coerce=lambda x: x if x is None else (x == 'True'),
        widget=forms.RadioSelect(attrs={'class': 'my-form'}),  # Use radio buttons for selection

        required=True,  # Set to True if the field is mandatory

    )

    class Meta:
        model = Mobile
        fields = ['brand', 'model', 'price', 'color', 'screen_size', 'is_available', 'country']
        widgets = {
            'country': CountrySelectWidget(),

        }
