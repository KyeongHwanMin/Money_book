from rest_framework import serializers
from moneybook.models import Expense


class ExpenseDefaultSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Expense
        fields = [
            'pk',
            'spent_at',
            'updated_at',
            'username',
            'email',
            'amount',
            'memo',
        ]


class ExpenseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'pk',
            'amount',
            'memo',
        ]


class ExpenseDetailSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Expense
        fields = ExpenseListSerializer.Meta.fields + [
            'username',
            'email',
            'spent_at',
            'updated_at',
        ]
