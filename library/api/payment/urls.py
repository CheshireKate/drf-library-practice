from rest_framework import routers

from library.api.payment.views import (
    PaymentViewSet
)

router = routers.DefaultRouter()
router.register("payment", PaymentViewSet)

app_name = "library.api.books"