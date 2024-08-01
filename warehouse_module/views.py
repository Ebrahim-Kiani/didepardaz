from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'warehouse_module/warehouse_brands_form.html')