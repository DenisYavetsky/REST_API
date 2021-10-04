import uuid as uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import get_object_or_404


class Account(models.Model):
    name = models.CharField(max_length=120, blank=False)
    number = models.CharField(max_length=20, blank=False, unique=True)
    overdraft = models.BooleanField(default=False)
    balance = models.IntegerField(default=0)

    def transfer(self, account_from, account_to, cost):
        acc = get_object_or_404(Account, number=account_from)
        acc.balance = acc.balance - cost
        acc.save()

        acc = get_object_or_404(Account, number=account_to)
        acc.balance = acc.balance + cost
        acc.save()

    def __str__(self):
        return self.number


class AccountOperation(models.Model):
    operation_id = models.CharField(max_length=40, blank=True)
    account_from = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='account_from')
    account_to = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='account_to')
    cost = models.IntegerField(default=0, blank=False)
    operation_dt = models.DateTimeField(auto_created=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uuid = str(uuid.uuid4())

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.operation_id == '':
            self.operation_id = self.uuid

        self.transfer(account_from=self.account_from,
                      account_to=self.account_to,
                      cost=self.cost)
        super().save()

    def transfer(self, account_from, account_to, cost):
        acc_from = get_object_or_404(Account, number=account_from)
        acc_to = get_object_or_404(Account, number=account_to)

        if acc_from == acc_to:
            raise ValidationError('access denied')
        if not (acc_from and acc_to):
            raise ValidationError('access denied')

        if acc_from.balance < int(cost) and acc_from.overdraft is False:
            raise ValidationError('access denied')

        Account().transfer(account_from, account_to, cost)

    def __str__(self):
        return self.operation_id
