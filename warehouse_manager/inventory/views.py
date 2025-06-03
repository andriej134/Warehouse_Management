from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Product, Order



def index(request):
    return render(request, 'inventory/index.html')

def product_order(request):
    diameters = [d[0] for d in Product.DIAMETER_CHOICES]
    shapes = [s[0] for s in Product.SHAPE_CHOICES]
    sizes = [s[0] for s in Product.SIZE_CHOICES]
    colors = [c[0] for c in Product.COLOR_CHOICES]
    errors = {}

    if request.method == "POST":
        order = Order(
            diameter=request.POST.get("diffuser_diameter"),
            shape=request.POST.get("diffuser_shape"),
            size=request.POST.get("diffuser_size"),
            color=request.POST.get("diffuser_color"),
            quantity_to_assemble=request.POST.get("quantity_to_assemble") or 0,
        )
        try:
            order.full_clean()  # WALIDACJA
            order.save()
            return redirect("inventory:product_order")
        except ValidationError as e:
            errors = e.message_dict

    orders = Order.objects.order_by('-created_at')[:10]  # ostatnie 10 zamówień
    return render(request, 'inventory/product_order.html', {
        'diameters': diameters,
        'shapes': shapes,
        'sizes': sizes,
        'colors': colors,
        'orders': orders,
    })

@login_required
def user_profile(request):
    return render(request, 'account/user_profile.html')

def delete_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        order.delete()
    return redirect("inventory:product_order")