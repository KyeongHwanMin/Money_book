from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def hsa_object_permission(self, request, view, obj):
        return obj.author == request.user
