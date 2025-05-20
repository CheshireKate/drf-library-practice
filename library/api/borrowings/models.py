from datetime import date

from django.db import models
from rest_framework.exceptions import ValidationError

from library.api.books.models import Book


class Borrowing(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="borrowings"
    )
    book_borrowed = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField()

    def clean(self):
        if self.expected_return_date <= self.borrow_date:
            raise ValidationError("Expected return date must be after borrow date.")

        if self.actual_return_date <= self.borrow_date:
            raise ValidationError("Actual return date cannot be before borrow date.")

        if self.book_borrowed.inventory < 1:
            raise ValidationError("The book is currently not available.")

    def decrease_book_number(self):
        book = self.book_borrowed
        book.inventory -= 1
        book.save()

    def attach_user_to_borrowing(self):
        self.user.borrowing = self


class ReturnBook(models.Model):
    returned_borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE)

    def clear(self):
        book = self.returned_borrowing.book_borrowed
        if book.actual_return_date:
            raise ValidationError("The book is already returned.")

    def increase_book_number(self):
        book = self.returned_borrowing.book_borrowed
        book.inventory += 1
        book.save()

    def detach_user_to_borrowing(self):
        user = self.user
        user.borrowing = None

    def deactivate_borrowing(self):
        self.returned_borrowing.is_active = False

    def set_actual_return_date(self):
        self.returned_borrowing.actual_return_date = date.today()
