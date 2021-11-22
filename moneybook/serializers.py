from rest_framework import serializers
from moneybook.models import Expense


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
