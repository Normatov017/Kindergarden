from django.shortcuts import render, redirect
from .models import Inventory
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required  # foydalanuvchi tizimga kirgan bo'lishi kerak
def inventory_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        delivery_date = request.POST.get('delivery_date')
        expiry_date = request.POST.get('expiry_date')
        source = request.POST.get('source')

        # Kiruvchi ma'lumotlarni validatsiya qilish (bu yerda oddiy holatda)
        if product_id and quantity and delivery_date and expiry_date and source:
            product = Product.objects.get(id=product_id)
            Inventory.objects.create(
                product=product,
                quantity=quantity,
                delivery_date=delivery_date,
                expiry_date=expiry_date,
                source=source,
                created_by=request.user
            )
            return redirect('inventory')  # saqlagandan keyin sahifani yangilash

    # Barcha inventory yozuvlarini olish
    inventories = Inventory.objects.all().order_by('-delivery_date')
    products = Product.objects.all()

    context = {
        'inventories': inventories,
        'products': products,
    }
    return render(request, 'inventory.html', context)
