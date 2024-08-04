from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, TemplateView
from .forms import BrandForm, MobileForm
from .models import Brand, Mobile
from rest_framework.generics import ListAPIView
from .serializers import WarehouseSerializer
from django.db.models import F


class BrandFormView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'warehouse_module/warehouse_brands_form.html'
    success_url = 'brand-form'


class MobileFormView(CreateView):
    model = Mobile
    form_class = MobileForm
    template_name = 'warehouse_module/warehouse_mobile_form.html'
    success_url = 'mobile-form'


class KoreanMobileAPIView(ListAPIView):
    queryset = Mobile.objects.filter(country='KR')
    serializer_class = WarehouseSerializer


class SameNationalAPIView(ListAPIView):
    queryset = Mobile.objects.filter(country=F('brand__country'))
    serializer_class = WarehouseSerializer


class MobileSearchView(View):
    def get(self, request):
        return render(request, 'warehouse_module/warehouse_search_form.html')

    def post(self, request):

        brand_name = request.POST.get('input-search')

        if brand_name:
            mobiles = Mobile.objects.select_related('brand').filter(brand__name__icontains=brand_name).all()

        else:
            mobiles = Mobile.objects.none()

        return render(request, 'warehouse_module/partial/partial.html', {'mobiles': mobiles})


class InformationMenuView(TemplateView):
    template_name = 'warehouse_module/warehouse_informations_menu.html'
