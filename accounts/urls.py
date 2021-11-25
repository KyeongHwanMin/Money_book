from django.urls import path

from accounts.views import RegisterUserView, LoginView, LogoutView

urlpatterns = [
    path('register-user/', RegisterUserView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]