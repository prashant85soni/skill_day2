from django.urls import path
from .views import ProductListCreateAPIview

urlpatterns = [
    path('products/', ProductListCreateAPIview.as_view(), name='product-list-create'),
]