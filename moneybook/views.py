from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from moneybook.moneybook_permissions import IsOwner

from moneybook.serializers import ExpenseDefaultSerializer, ExpenseListSerializer, ExpenseDetailSerializer
from moneybook.models import Expense
from rest_framework.viewsets import ModelViewSet


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseDefaultSerializer

    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['memo']

    def get_serializer_class(self):
        if self.action == 'list':
            return ExpenseListSerializer
        elif self.action == 'retrieve':
            return ExpenseDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()

        is_deleted = False

        query_param_is_deleted = self.request.query_params.get('is_deleted')
        if query_param_is_deleted == 'true':
            is_deleted = True

        queryset = queryset.filter(user=self.request.user, is_deleted=is_deleted)
        return queryset

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    @action(detail=True, methods=['POST'], url_path='restore')
    def restore(self, request, pk):
        instance = get_object_or_404(self.queryset.filter(user=self.request.user, is_deleted=True), pk=pk)
        instance.is_deleted = False
        instance.save(update_fields=['is_deleted'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    #
    # @action(detail=True, methods=['GET]'])
    # def detailview(self, request, pk):
    #     instance = self.get_object()
    #     instance.is_deleted = False
    #     instance.save(update_fields=['is_deleted'])
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


# class DetailView(APIView):
#     queryset = Expense.objects.all()
#     serializer_class = DetailViewSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         is_deleted = False
#
#         query_param_is_deleted = self.request.query_params.get('is_deleted')
#         if query_param_is_deleted == 'true':
#             is_deleted = True
#
#         queryset = queryset.filter(user=self.request.user, is_deleted=is_deleted)
#         return queryset




