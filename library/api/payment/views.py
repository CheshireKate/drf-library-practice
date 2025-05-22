from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from library.api.payment.models import Payment
from library.api.payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser]
