from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow safe methods for everyone.
    Only admins can edit or delete wishes.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
