from rest_framework import permissions


# class IsOwner(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#
#         # if (request.method == 'DELETE'):
#         #     return request.user.is_superuser
#         # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인
#         return obj.user == request.user

class IsOwner(permissions.BasePermission):
    def hsa_object_permission(self, request, view, obj):
        return obj.author == request.user
