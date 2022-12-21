from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'permission', views.PermissionViewSet, basename='permission')

urlpatterns = [ 
   path('', include(router.urls)),
   path('permission_user/', views.PermissionUser.as_view()),
   path('permission_user/<id>/', views.PermissionUser.as_view()),
]