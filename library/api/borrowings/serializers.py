from rest_framework import serializers

from library.api.books.models import Book
from library.api.borrowings.models import Borrowing


class BorrowingSerializer(serializers.Serializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), many=False, slug_field="title")

    class Meta:
        model = Borrowing
        fields = ["book", "borrow_date", "expected_return_date", "actual_return_date"]