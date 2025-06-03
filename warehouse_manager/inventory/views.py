from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'inventory/index.html')

def product_order(request):
    return render(request, 'inventory/product_order.html')

@login_required
def user_profile(request):
    return render(request, 'account/user_profile.html')