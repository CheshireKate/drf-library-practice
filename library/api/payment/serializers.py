from rest_framework import serializers

from library.api.payment.models import Payment


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ["status", "type", "borrowing_id", "session_url", "session_id", "money_to_pay"]