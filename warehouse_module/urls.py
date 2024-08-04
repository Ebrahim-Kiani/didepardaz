from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.BrandFormView.as_view(), name='brand-form'),
    path('mobile/', views.MobileFormView.as_view(), name='mobile-form'),
    path('korean-mobile/', views.KoreanMobileAPIView.as_view(), name='koran-mobile-list'),
    path('same-national/', views.SameNationalAPIView.as_view(), name='same-national-list'),
    path('search-mobile/', views.MobileSearchView.as_view(), name='search-mobile'),
    path('informaiton-menu/', views.InformationMenuView.as_view(), name='inforamtoin-menu')
]