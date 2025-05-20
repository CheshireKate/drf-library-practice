from rest_framework import status
from rest_framework.test import APIClient

from unittest import TestCase

from rest_framework.reverse import reverse

from library.api.books.models import Book, Author
from library.api.users.models import User

ADMIN_URL = reverse("admin/")
BOOK_CREATE = reverse("books:create/")
BOOKS_URL = reverse("theater:book-list")


def book_detail_url(book_id):
    return reverse("books:user-detail", kwargs={"id": book_id})


class UnauthenticatedTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(ADMIN_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_created_if_not_admin(self):
        res = self.client.get(BOOK_CREATE)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_if_not_admin(self):
        author = Author.objects.create(last_name="Meyer", first_name="Stephenie")
        book = Book.objects.create(
            title="Twilight", author=author, cover="soft", inventory=10, daily_fee=0.3
        )
        url = book_detail_url(book.id)
        res = self.client.patch(url, {"title": "Not Twilight"})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class IfAdminTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com", password="adminpass"
        )
        self.client.force_authenticate(self.admin_user)

    def test_can_create_book(self):
        author = Author.objects.create(last_name="Meyer", first_name="Stephenie")
        book = Book.objects.create(
            title="Twilight", author=author, cover="soft", inventory=10, daily_fee=0.3
        )
        self.admin_user.put(book)
        res = self.client.get(BOOKS_URL)
        self.assertIn(book, res)

    def test_can_delete_book(self):
        author = Author.objects.create(last_name="Meyer", first_name="Stephenie")
        book = Book.objects.create(
            title="Twilight", author=author, cover="soft", inventory=10, daily_fee=0.3
        )
        self.admin_user.delete(book)
        res = self.client.get(BOOKS_URL)
        self.assertNotIn(book, res)
        res = book_detail_url(book.url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
