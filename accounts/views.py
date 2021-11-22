from django.contrib.auth import get_user_model, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import RegisterUserSerializer, LoginSerializer

User = get_user_model()


class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['email']
        if User.objects.filter(username=username).exists():
            return Response(data={'error': '이미 존재하는 username 을 입력하였습니다.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        User.objects.create_user(username=username,
                                 password=serializer.validated_data['password'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.get(username=serializer.validated_data['email'])
        except User.DoesNotExist:
            return Response(data={'error': '잘못 입력하였습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(serializer.validated_data['password']):
            return Response(data={'error': '잘못 입력하였습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        return Response(status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
