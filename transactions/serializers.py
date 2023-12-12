from rest_framework import serializers
from .models import Transactions, TransactionCategories, UserBalance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategories
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=TransactionCategories.objects.all())

    class Meta:
        model = Transactions
        fields = '__all__'


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = '__all__'
