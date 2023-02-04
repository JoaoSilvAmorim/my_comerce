from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import Permission
from django.http import HttpResponseForbidden
from .models import User as Users
from .serializer import *

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    @action(detail=False, methods=['post'])
    def roles_permission(self, request, client = None):
        try:
            permission = request.data['permission']
            if permission in list(map(lambda item: item.split('.')[-1], list(request.user.get_all_permissions()))):
                return Response(status=status.HTTP_200_OK)
            
            return HttpResponseForbidden("Seu usuario não tem permissão para acessar essa view...")
        except:
            return HttpResponseForbidden("Seu usuario não tem permissão para acessar essa view...")


class PermissionUser(APIView):
    def get_user(self, id):
        try:
            return Users.objects.filter(id=id).get()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, client=None, id=None):
            print(id)
            user = self.get_user(id)
            serializer = PermissionUserSerializer.to_representation(self, user)
            return Response(serializer["data"])
        
    def put(self, request, client = None, id = None):
        user = Users.objects.filter(id=id).get()
        serializer = PermissionUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.update(user, request.data)
                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client = None, id=None):
        user = Users.objects.filter(id=id).get()
        serializer = PermissionUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.delete(user, request.data)
                return Response(status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
