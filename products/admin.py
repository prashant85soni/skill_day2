from django.contrib import admin
from products.models import Products
# Register your models here.

class ProductManager(admin.ModelAdmin):
    list_display=('name','price','stock')
    list_filter=('is_active',)
    search_fields=('name',)
    ordering=('created_at',)
    



admin.site.register(Products,ProductManager)