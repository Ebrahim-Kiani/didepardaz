from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .forms import BrandForm, MobileForm
from .models import Brand, Mobile
from rest_framework.generics import ListAPIView
from .serializers import WarehouseSerializer
from django.db.models import F
from rest_framework.permissions import BasePermission
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class BrandFormView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'warehouse_module/warehouse_brands_form.html'
    success_url = reverse_lazy('brand-form')


@method_decorator(login_required, name='dispatch')
class MobileFormView(CreateView):
    model = Mobile
    form_class = MobileForm
    template_name = 'warehouse_module/warehouse_mobile_form.html'
    success_url = reverse_lazy('mobile-form')


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class InformationMenuView(TemplateView):
    template_name = 'warehouse_module/warehouse_informations_menu.html'


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow any user to perform read-only actions
        if request.method in SAFE_METHODS:
            return True
        # Only allow admin users to perform write actions
        return request.user and request.user.is_staff


class KoreanMobileAPIView(ListAPIView):
    queryset = Mobile.objects.filter(country='KR')
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]


class SameNationalAPIView(ListAPIView):
    queryset = Mobile.objects.filter(country=F('brand__country'))
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]
