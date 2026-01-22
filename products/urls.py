from django.urls import path
from .views import ProductListCreateAPIview, ProductRetrievewUpdateDestroyAPIview

urlpatterns = [
    path('products/', ProductListCreateAPIview.as_view(), name='product-list-create'),
    #path('products/<int:pk>',ProductRetrievewUpdateDestroyAPIview.as_view, name='product-retrive-update')
    path('products/int:pk/', ProductRetrievewUpdateDestroyAPIview.as_view(), name='product-retreive-update'),
]