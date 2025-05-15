from django.urls import path

from library.api.books.views import BookListView, BookDetailView, BookDeleteView, BookCreateView, BookUpdateView

urlpatterns = [
    path("books/", BookListView.as_view(), basename="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), basename="book-detail"),
    path("books/create/", BookCreateView.as_view(), basename="book-create"),
    path("books/update/", BookUpdateView.as_view(), basename="book-update"),
    path("books/delete/", BookDeleteView.as_view(), basename="book-delete"),
]

app_name = "library.api.books"
