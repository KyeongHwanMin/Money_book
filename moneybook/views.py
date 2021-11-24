from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.response import Response

from moneybook.moneybook_permissions import IsAuthorOrReadonly

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

    permission_classes = [IsAuthorOrReadonly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['memo']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return Expense.objects.filter(is_deleted=False, user_id=self.request.user.id)

    # def get_queryset(self):
    #     qs = self.queryset.filter(user=self.request.user, is_deleted=False)
    #     return qs

    # 가계부 리스트 출력, 값 추가
    @action(detail=False, methods=['GET', 'POST'])
    def expense_list(self, request):
        if request.method == 'GET':
            qs = self.get_queryset().filter(is_deleted=False, user_id=self.request.user.id)
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data)
        else:
            serializer = ExpenseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)

    # 삭제된 리스트 출력
    @action(detail=False, methods=['GET'])
    def deleted(self, request):
        qs = self.get_queryset().filter(is_deleted=True, user_id=self.request.user.id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # 삭제
    @action(detail=True, methods=['PATCH'])
    def set_delete(self, request, pk):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save(update_fields=['is_deleted'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # 삭제 복구
    @action(detail=True, methods=['PATCH'])
    def restore(self, request, pk):
        instance = self.get_object()
        instance.is_deleted = False
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
# @api_view(['GET','POST'])
# def Expense_list(request):
#     if request.method == 'GET':
#         queryset = Expense.objects.filter(is_deleted=False, user_id=request.user.id)
#         serializer = ExpenseSerializer(queryset, many=True)
#         return Response(serializer.data)
#     else:
#         serializer = ExpenseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
# @api_view(['GET', 'PUT', "DELETE"])
# def Expense_list_deleted(request):
#
#     if request.method == 'GET':
#         queryset = Expense.objects.filter(is_deleted=True, user_id=request.user.id)
#         serializer = ExpenseSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         queryset = Expense.objects.filter(is_deleted=True, user_id=request.user.id)
#         serializer = ExpenseSerializer(queryset, many=True)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         Expense.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
#


# @api_view(['GET', 'POST'])
# def Expense_list(request):
#     if request.method == 'GET':
#         serializer = ExpenseSerializer(Expense.objects.all(), many=True)
#         return Response(serializer.data)
#
#     else:
#         serializer = ExpenseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def Expense_detail(request, pk):
#     post = get_object_or_404(Expense, pk=pk)
#
#     if request.method == 'GET':
#         serializer = ExpenseSerializer(Expense)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ExpenseSerializer(Expense, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         post.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
