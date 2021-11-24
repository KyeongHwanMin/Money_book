from rest_framework.routers import DefaultRouter
from django.urls import path, include
from moneybook import views
# from moneybook.views import Myview

router = DefaultRouter()
router.register('Expense', views.ExpenseViewSet)


urlpatterns =[
     path('',include(router.urls)),
     # path('Myview', Myview.as_view(), name='Myview'),
     # path('Expense_list/', views.Expense_list),
     #
     #
     # path('Expense_detail/', views.Expense_detail),
     #path('Expense_list_deleted/', views.Expense_list_deleted),
]