from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.urls import reverse
from django.views.decorators.http import require_POST
from permissions.permisssion import role_required


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






def products_view(request):
    products = Product.objects.all().order_by('-created_at')

    # Qidiruv
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query)

    # Holat bo‘yicha filtr
    status_filter = request.GET.get('status')
    if status_filter:
        filtered_products = []
        for product in products:
            if product.weight <= product.minimum_threshold / 2 and status_filter == 'danger':
                filtered_products.append(product)
            elif product.minimum_threshold / 2 < product.weight <= product.minimum_threshold and status_filter == 'warning':
                filtered_products.append(product)
            elif product.weight > product.minimum_threshold and status_filter == 'safe':
                filtered_products.append(product)
        products = filtered_products

    # POST orqali qo‘shish
    if request.method == "POST":
        name = request.POST.get('product-name')
        weight = request.POST.get('product-weight')
        delivery_date = request.POST.get('delivery-date')
        Product.objects.create(name=name, weight=weight, delivery_date=delivery_date)
        return redirect('products')

    return render(request, 'products.html', {'products': products})

