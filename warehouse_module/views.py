from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import BrandForm, MobileForm
from .models import Brand, Mobile


class BrandFormView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'warehouse_module/warehouse_brands_form.html'
    success_url = 'brands-form'


class MobileFormView(CreateView):
    model = Mobile
    form_class = MobileForm
    template_name = 'warehouse_module/warehouse_mobile_form.html'
    success_url = 'mobile-form'
