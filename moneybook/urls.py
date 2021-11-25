from rest_framework.routers import DefaultRouter
from django.urls import path, include
from moneybook import views
# from moneybook.views import Myview

router = DefaultRouter()
router.register('expense', views.ExpenseViewSet)


urlpatterns = [
     # router.urls 호출시 생성되는 url, view 매핑

     # REST Architecture style
     # [v] GET /expense/       => ExpenseViewSet 의 list, activate records
     # [v] GET /expense/?is_deleted=true       => ExpenseViewSet 의 list, deleted_records

     # [v] POST /expense/      => ExpenseViewSet 의 create
     # [default] GET /expense/1/      => ExpenseViewSet 의 retrieve
     # [default] PUT /expense/1/      => ExpenseViewSet 의 update
     # [default] PATCH /expense/1/    => ExpenseViewSet 의 partial_update
     # [v] DELETE /expense/1/   => ExpenseViewSet 의 destroy

     # Custom API
     # [v] POST /expense/1/restore/  =>  ExpenseViewSet 의 restore

     path('', include(router.urls)),
     # path('Myview', Myview.as_view(), name='Myview'),
     # path('Expense_list/', views.Expense_list),
     #
     #
     # path('Expense_detail/', views.Expense_detail),
     #path('Expense_list_deleted/', views.Expense_list_deleted),
]