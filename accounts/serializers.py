from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import Account, AccountOperation


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'name', 'number', 'overdraft'
        ]


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountOperation
        fields = '__all__'

    def validate(self, attrs):
        acc_from = get_object_or_404(Account, number=attrs['account_from'])
        acc_to = get_object_or_404(Account, number=attrs['account_to'])

        if acc_from == acc_to:
            raise serializers.ValidationError('access denied')
        if not (acc_from and acc_to):
            raise serializers.ValidationError('access denied')

        if acc_from.balance < int(attrs['cost']) and acc_from.overdraft is False:
            raise serializers.ValidationError('access denied')
        return attrs


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance']
