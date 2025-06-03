from django.contrib import admin
from django.urls import path, include


app_name = 'inventory'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
]

admin.site.site_header = "AFDynamic – Panel administracyjny"
admin.site.site_title = "AFDynamic Admin"
admin.site.index_title = "Administracja stroną"