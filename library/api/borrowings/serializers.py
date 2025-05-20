from rest_framework import serializers

from library.api.books.models import Book
from library.api.borrowings.models import Borrowing, ReturnBook
from library.api.users.models import User


class BorrowingSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), many=False, slug_field="id")
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), many=False, slug_field="title")

    class Meta:
        model = Borrowing
        fields = ["user", "book", "borrow_date", "expected_return_date", "actual_return_date", "is_active"]


class CreateBorrowingSerializer(BorrowingSerializer):
    ...


class ReturnBookSerializer(serializers.Serializer):
    returned_borrowing = serializers.SlugRelatedField(queryset=Borrowing.objects.all(), many=False, slug_field="id")

    class Meta:
        model = ReturnBook
        fields = ["returned_borrowing"]