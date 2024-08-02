from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.BrandFormView.as_view(), name='brand-form'),
    path('mobile/', views.MobileFormView.as_view(), name='mobile-form')
]