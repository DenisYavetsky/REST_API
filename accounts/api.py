from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Account, AccountOperation
from .serializers import AccountSerializer, TransferSerializer, BalanceSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_queryset(self):
        queryset = Account.objects.all()
        return queryset


class TransferViewSet(viewsets.ModelViewSet):
    queryset = AccountOperation.objects.all()
    serializer_class = TransferSerializer


class BalanceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BalanceSerializer
    queryset = Account.objects.all()

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_queryset(self):
        queryset = Account.objects.all()
        return queryset
