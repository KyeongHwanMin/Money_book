from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # if (request.method == 'DELETE'):
        #     return request.user.is_superuser
        # 요청자(request.user)가 객체(Blog)의 user와 동일한지 확인
        return obj.user == request.user
#
# class IsAuthorOrReadonly(permissions.BasePermission):
#     # 인증이 되어야만, 목록조회/포스팅등록을 허용
#     def has_permission(self, reqeust, view):
#         return request.user and request.user.is_authenticated
#
#
#     def hsa_object_permission(self, reqeust, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user