from rest_framework import serializers

from accounts.models import User


# class RegisterUserSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             name=validated_data['name'],
#             password=validated_data['password']
#         )
#         return user
#
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password']


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

#
class RegisterUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
