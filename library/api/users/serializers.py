from rest_framework import serializers

from library.api.users.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"