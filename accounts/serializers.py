from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)