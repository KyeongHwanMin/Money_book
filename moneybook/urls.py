from rest_framework.routers import DefaultRouter
from django.urls import path, include
from moneybook import views

router = DefaultRouter()
router.register('Expense', views.ExpenseViewSet)


urlpatterns =[
     path('',include(router.urls)),
     path('Expense1/', views.Expense_list),
     path('Expense2/', views.Expense_detail),
]