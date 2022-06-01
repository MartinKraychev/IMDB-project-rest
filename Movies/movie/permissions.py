from rest_framework import permissions


class IsOwnerOfObject(permissions.BasePermission):
    """
    Custom permission to validate if request user is owner
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
