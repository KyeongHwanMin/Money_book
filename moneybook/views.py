from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.response import Response

from moneybook.permissions import IsOwner
from moneybook.serializers import ExpenseSerializer
from moneybook.models import Expense
from rest_framework.viewsets import ModelViewSet


#
# class ExpenseListAPIView(generics.ListAPIView):
#     queryset = Expense.objects.filter(is_deleted=True)
#     serializer_class = ExpenseSerializer

#
# User = get_user_model()
#
#
# class Myview(generics.ListAPIView):
#     serializer_class = ExpenseSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         # obj = User.objects.get(username=self.request.user.username)
#         # self.check_object_permissions(self.request, obj)
#         # return obj
#         return Expense.objects.filter(user_id=1)


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # permission_classes = [IsOwner]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['memo']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    # def get_queryset(self):
    #     return Expense.objects.filter(is_deleted=True, user_id=self.request.user.id)
    # def get_queryset(self):
    #     qs = self.queryset.filter(user=self.request.user, is_deleted=False)
    #     return qs

    @action(detail=False, methods=['GET'])
    def deleted(self, request):
        qs = self.get_queryset().filter(is_deleted=True, user_id=self.request.user.id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_deleted=False, user_id=self.request.user.id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save(update_fields=['is_deleted'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# 모든 값 출
# class ExpenseViewSet(ModelViewSet):
#     # queryset = Expense.objects.all()
#     queryset = Expense.objects.filter()
#     serializer_class = ExpenseSerializer
#     permission_classes = [IsOwner]  # 인증이 됨을 보장
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['memo']
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)
#
#     @action(detail=False, methods=['GET'])
#     def public(self, request):
#         qs = self.get_queryset().filter(is_deleted=True)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['PATCH'])
#     def set_public(self, request, pk):
#         instance = self.get_object()
#         instance.is_deleted = True
#         instance.save(update_fields=['is_deleted'])
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


# Expense_list = ExpenseViewSet.as_view({
#     'get': 'list',
# })
# Expense_detail = ExpenseViewSet.as_view({
#     'get': 'retrieve',
# })
# 해당 id 리스트 출력
# @api_view(['GET'])
# def Expense_list(request):
#     queryset = Expense.objects.filter(is_deleted=False)
#     serializer = ExpenseSerializer(queryset, many=True)
#     return Response(serializer.data)

@api_view(['GET', 'POST'])
def Expense_list(request):
    if request.method == 'GET':
        serializer = ExpenseSerializer(Expense.objects.all(), many=True)
        return Response(serializer.data)

    else:
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def Expense_detail(request, pk):
    post = get_object_or_404(Expense, pk=pk)

    if request.method == 'GET':
        serializer = ExpenseSerializer(Expense)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ExpenseSerializer(Expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
