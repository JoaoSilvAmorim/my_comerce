import jwt
from .settings import SECRET_KEY
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        username = self.user.username
        perms = list(self.user.get_all_permissions())
        #groups = self.user.groups.values_list('name', flat=True)
        
        return {
          'access': str(refresh.access_token),
          'refresh': str(refresh),
          'user': jwt.encode({
            'username': username, 
            'perms': perms
          }, SECRET_KEY),
        }


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer