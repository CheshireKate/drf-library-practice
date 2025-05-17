from django.urls import path

from library.api.borrowings.views import BorrowingListView, BorrowingDetailView

urlpatterns = [
    path("borrowings/", BorrowingListView.as_view(), basename="borrowing-list"),
    path("borrowings/<int:pk>/", BorrowingDetailView.as_view(), basename="borrowing-detail"),
]

app_name = "library.api.borrowings"