from django.contrib import admin
from django.urls import path, include


app_name = 'inventory'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),

]