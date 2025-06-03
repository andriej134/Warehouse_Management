from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order


def index(request):
    return render(request, 'inventory/index.html')

def product_order(request):
    diameters = [d[0] for d in Product.DIAMETER_CHOICES]
    shapes = [s[0] for s in Product.SHAPE_CHOICES]
    sizes = [s[0] for s in Product.SIZE_CHOICES]
    colors = [c[0] for c in Product.COLOR_CHOICES]

    if request.method == "POST":
        Order.objects.create(
            diameter=request.POST.get("diffuser_diameter"),
            shape=request.POST.get("diffuser_shape"),
            size=request.POST.get("diffuser_size"),
            color=request.POST.get("diffuser_color"),
            quantity_to_assemble=request.POST.get("quantity_to_assemble") or 0,
        )
        return redirect("inventory:product_order")  # lub inna strona z potwierdzeniem

    return render(request, 'inventory/product_order.html', {
        'diameters': diameters,
        'shapes': shapes,
        'sizes': sizes,
        'colors': colors,
    })

@login_required
def user_profile(request):
    return render(request, 'account/user_profile.html')