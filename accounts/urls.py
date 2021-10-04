from rest_framework import routers
from .api import AccountViewSet, TransferViewSet, BalanceViewSet

router = routers.DefaultRouter()

router.register('api/v1/account/account', AccountViewSet, 'account')
router.register('api/v1/account/transfer', TransferViewSet, 'transfer')
router.register('api/v1/account/balance', BalanceViewSet, 'balance')

urlpatterns = router.urls
