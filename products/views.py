from django.shortcuts import render
from rest_framework import viewsets
from .models import products
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=products.objects.all()
    serializer_class= ProductSerializer

# Create your views here.
