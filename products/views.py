from rest_framework.viewsets import ModelViewSet
from .models import Product as Products
from rest_framework.response import Response
from rest_framework import status
from .serializer import *

from rest_framework.decorators import action

class ProductViewSet(ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    @action(detail=True, methods=['get'])
    def products_user(self, request, client = None, pk = None):
        products = Products.objects.filter(user_id=pk)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)