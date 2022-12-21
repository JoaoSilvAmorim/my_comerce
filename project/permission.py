from rest_framework.permissions import BasePermission

class PermissionView(BasePermission):
  def has_permission(self, request, view):
    if view.permission in list(request.user.get_all_permissions()):
      return True
    return False