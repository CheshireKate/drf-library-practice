from django.urls import path

from library.api.borrowings.views import (
    BorrowingListView,
    BorrowingDetailView,
    BorrowingCreateView,
    ReturnBookCreateView,
    ReturnDetailView,
)

urlpatterns = [
    path("borrowings/", BorrowingListView.as_view(), name="borrowing-list"),
    path(
        "borrowings/<int:pk>/", BorrowingDetailView.as_view(), name="borrowing-detail"
    ),
    path("borrowings/create/", BorrowingCreateView.as_view(), name="borrowing-create"),
    path("return/create/", ReturnBookCreateView.as_view(), name="return-create"),
    path("return/<int:pk>/", ReturnDetailView.as_view(), name="return-detail"),
]

app_name = "library.api.borrowings"
