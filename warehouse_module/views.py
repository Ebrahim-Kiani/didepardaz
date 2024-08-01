from django.shortcuts import render, redirect
from .forms import BrandForm


def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')  # Replace with your actual success URL
    else:
        form = BrandForm()
    return render(request, 'warehouse_module/warehouse_brands_form.html', {'form': form})
