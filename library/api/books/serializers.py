from rest_framework import serializers

from library.api.books.models import Author, Book


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ["last_name", "first_name"]


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ["title", "author", "cover", "inventory", "daily_fee"]
