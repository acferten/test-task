from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
