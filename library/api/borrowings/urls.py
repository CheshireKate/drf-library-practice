from django.urls import path

from library.api.borrowings.views import BorrowingListView, BorrowingDetailView, BorrowingCreateView, \
    ReturnBookCreateView, ReturnDetailView

urlpatterns = [
    path("borrowings/", BorrowingListView.as_view(), basename="borrowing-list"),
    path("borrowings/<int:pk>/", BorrowingDetailView.as_view(), basename="borrowing-detail"),
    path("borrowings/create/", BorrowingCreateView.as_view(), basename="borrowing-create"),
    path("return/create/", ReturnBookCreateView.as_view(), basename="return-create"),
    path("return/<int:pk>/", ReturnDetailView.as_view(), basename="return-detail"),
]

app_name = "library.api.borrowings"