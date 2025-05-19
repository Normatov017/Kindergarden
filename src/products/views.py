from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.urls import reverse
from django.views.decorators.http import require_POST


def products_view(request):
    products = Product.objects.all().order_by('-created_at')

    # Qo‘shish (POST)
    if request.method == "POST":
        name = request.POST.get('product-name')
        weight = request.POST.get('product-weight')
        delivery_date = request.POST.get('delivery-date')
        Product.objects.create(name=name, weight=weight, delivery_date=delivery_date)
        return redirect('products')

    return render(request, 'products.html', {'products': products})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(request.POST.get)
    if request.method == "POST":
        product.name = request.POST.get('product-name')
        product.weight = request.POST.get('product-weight')
        product.delivery_date = request.POST.get('delivery-date')
        if product.name and product.weight and product.delivery_date:
            product.save()
            return redirect('products')
        print(product.name)
    return render(request, 'edit_product.html', {'product': product})


@require_POST
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')