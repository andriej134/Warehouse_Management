from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

def index(request):
    return render(request, 'inventory/index.html')

def product_order(request):
    diameters = [d[0] for d in Product.DIAMETER_CHOICES]
    shapes = [s[0] for s in Product.SHAPE_CHOICES]
    sizes = [s[0] for s in Product.SIZE_CHOICES]
    colors = [c[0] for c in Product.COLOR_CHOICES]
    return render(request, 'inventory/product_order.html', {
        'diameters': diameters,
        'shapes': shapes,
        'sizes': sizes,
        'colors': colors,
    })

@login_required
def user_profile(request):
    return render(request, 'account/user_profile.html')