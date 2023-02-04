"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .util import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path, include, re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Dummy API",
      default_version='v1',
      description="Dummy description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dummy.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^playground/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)