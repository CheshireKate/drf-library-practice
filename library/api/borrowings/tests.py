from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from unittest import TestCase

from rest_framework.reverse import reverse

from library.api.books.models import Author, Book
from library.api.borrowings.models import Borrowing, ReturnBook
from library.api.users.models import User

ADMIN_URL = reverse("admin/")
BORROWING_CREATE = reverse("borrowings:create/")
BORROWING_URL = reverse("borrowings:borrowing-list")

def borrowing_detail_url(borrowing_id):
    return reverse("borrowings:borrowing-detail", kwargs={"id": borrowing_id})

def return_url(return_id):
    return reverse("borrowings:return-detail", kwargs={"id": return_id})


class UnauthenticatedTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        ),
        self.client.force_authenticate(self.user)

    def test_created_if_not_admin(self):
        res = self.client.get(BORROWING_CREATE)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class IfAdminTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        self.client.force_authenticate(self.admin_user)

    def test_can_create_return(self):
        author = Author.objects.create(last_name="Meyer", first_name="Stephenie")
        book = Book.objects.create(title="Twilight",
                                   author=author,
                                   cover="soft",
                                   inventory=10,
                                   daily_fee=0.3
                                   )
        borrowing = Borrowing.objects.create(user=get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        ),
                                             book_borrowed=book,
                                             borrow_date=2025-1-3,
                                             expected_return_date=2025-1-30,
                                             actual_return_date=2025-1-29,
                                             is_active=True,
                                             )
        return_book = ReturnBook(returned_borrowing=borrowing)

        self.admin_user.put(author)
        self.admin_user.put(book)
        self.admin_user.put(borrowing)
        self.admin_user.put(return_book)

        return_url_ = return_url(return_book.id)
        res = self.client.get(return_url_)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class NotOwner(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        ),
        self.client.force_authenticate(self.user)


    def test_cant_see_other_borrowing(self):
        another_user = get_user_model().objects.create_user(
            "test@test.comm",
            "testpasss",
        ),
        author = Author.objects.create(last_name="Meyer", first_name="Stephenie")
        book = Book.objects.create(title="Twilight",
                                   author=author,
                                   cover="soft",
                                   inventory=10,
                                   daily_fee=0.3
                                   )
        borrowing = Borrowing.objects.create(user=another_user,
            book_borrowed=book,
            borrow_date=2025 - 1 - 3,
            expected_return_date=2025 - 1 - 30,
            actual_return_date=2025 - 1 - 29,
            is_active=True,
        )
        borrowing_url = borrowing_detail_url(borrowing.id)
        res = self.client.get(borrowing_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
