from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    # Dodaj inne widoki jeśli są potrzebne:
    # path('products/', views.products, name='products'),
    # path('categories/', views.categories, name='categories'),
    # path('reports/', views.reports, name='reports'),
    # path('settings/', views.settings, name='settings'),
]