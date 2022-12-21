from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth.models import Permission
from .db_query import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        validated_data['is_active'] = True
        user = User.objects.create(**validated_data)
        return user
        
class PermissionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_permissions', )

    def update(self, instance, validated_data):
        for perm in validated_data['user_permissions']:
            permission = Permission.objects.get(id=perm)
            instance.user_permissions.add(permission)
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        for perm in validated_data['user_permissions']:
            permission = Permission.objects.get(id=perm)
            instance.user_permissions.remove(permission)
        instance.save()
        return instance

    def to_representation(self, instance):
        query = query_permission_user(id=instance.id)
        permission_user = User.objects.raw(query)
        data = []
        for perm in permission_user:
            permission = Permission.objects.get(id=perm.id)
            data.append({"id": permission.id, "name": permission.name, "code_name": permission.codename})
        return {
            'data': data
        }

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename', 'name', )
        
    def create(self, validated_data):
        perm_data = Permission.objects.filter(codename__contains='permission')[0]
        validated_data['content_type_id'] = perm_data.content_type_id
        perm = Permission.objects.create(**validated_data)
        return perm