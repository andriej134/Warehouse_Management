from django.shortcuts import render

def index(request):
    return render(request, 'inventory/index.html')

def product_order(request):
    return render(request, 'inventory/product_order.html')