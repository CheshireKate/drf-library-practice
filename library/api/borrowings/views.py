from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from library.api.borrowings.models import Borrowing, ReturnBook
from library.api.borrowings.serializers import BorrowingSerializer, CreateBorrowingSerializer, ReturnBookSerializer
from library.permissions import IsOwner


class BorrowingListView(generics.ListAPIView):
    serializer_class = BorrowingSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            user_id = self.request.query_params.get("user_id")
            if user_id:
                return Borrowing.objects.filter(user__id=user_id)
            else:
                return Borrowing.objects.all()


class BorrowingDetailView(generics.RetrieveAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAdminUser, IsAuthenticated, IsOwner]


class BorrowingCreateView(generics.CreateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = CreateBorrowingSerializer
    permission_classes = [IsAdminUser]


class ReturnBookCreateView(generics.CreateAPIView):
    queryset = ReturnBook.objects.all()
    serializer_class = ReturnBookSerializer
    permission_classes = [IsAdminUser]
