from django.contrib.auth import get_user_model
from rest_framework import serializers

from moneybook.models import Expense


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id', 'username', 'email']


class ExpenseSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Expense
        fields = [
            'pk',
            'username',
            'email',
            'amount',
            'spent_at',
            'memo',
            'is_deleted',

        ]
