from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializer import ProductSerializer
# Create your views here.

class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    