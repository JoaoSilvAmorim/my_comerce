from rest_framework.viewsets import ModelViewSet
from .models import Product as Products
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from project.permission import PermissionView
    
class ProductViewSet(ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()