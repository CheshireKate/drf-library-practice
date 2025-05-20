from unittest import TestCase

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from library.api.books.models import Author, Book
from library.api.borrowings.models import ReturnBook, Borrowing
from library.api.users.models import User



class BorrowingLogics(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        self.client.force_authenticate(self.admin_user)

    def test_borrowing_status_changes_if_returned(self):
        author = Author.objects.create(last_name="Meyer", first_name="Stephenie")
        book = Book.objects.create(title="Twilight",
                                   author=author,
                                   cover="soft",
                                   inventory=10,
                                   daily_fee=0.3
                                   )
        user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        ),
        borrowing = Borrowing.objects.create(user=user,
                                             book_borrowed=book,
                                             borrow_date=2025 - 1 - 3,
                                             expected_return_date=2025 - 1 - 30,
                                             actual_return_date=2025 - 1 - 29,
                                             is_active=True,
                                             )
        return_book = ReturnBook(returned_borrowing=borrowing)
        self.assertNotIn(borrowing, self.user.borrowings)
