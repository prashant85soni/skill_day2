from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializer import ProductSerializer
from rest_framework.filters import SearchFilter
# Create your views here.

class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[SearchFilter]
    SearchField=['name', 'description']
    
class ProductRetrievewUpdateDestroyAPIview(generics.RetrieveUpdateDestroyAPIView):
     queryset=Products.objects.all()
     serializer_class=ProductSerializer
     SearchField=['name'] 
       