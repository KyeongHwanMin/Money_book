from rest_framework.routers import DefaultRouter
from django.urls import path, include
from moneybook import views

router = DefaultRouter()
router.register('expense', views.ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
