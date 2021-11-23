from .models import User
from .serializers import RegisterUserSerializer, LoginSerializer

from rest_framework import generics, status

from django.contrib.auth import get_user_model, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView

# from accounts.serializers import RegisterUserSerializer, LoginSerializer


# class RegisterUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterUserSerializer

# User = get_user_model()
#
#
class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        if User.objects.filter(email=email).exists():
            return Response(data={'error': '이미 존재하는 email 을 입력하였습니다.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        User.objects.create_user(name=name,email=email,
                                 password=serializer.validated_data['password'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(email=serializer.validated_data['email'])
        except User.DoesNotExist:
            return Response(data={'error': '잘못 입력하였습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(serializer.validated_data['password']):
            return Response(data={'error': '잘못 입력하였습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        return Response(status=status.HTTP_200_OK)

#
# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response(status=status.HTTP_200_OK)
