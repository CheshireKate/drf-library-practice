from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from library.api.borrowings.models import Borrowing
from library.api.borrowings.serializers import BorrowingSerializer
from library.permissions import IsOwner


class BorrowingListView(generics.ListAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAdminUser]


class BorrowingDetailView(generics.RetrieveAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAdminUser, IsOwner]