from django.db import models
from rest_framework.exceptions import ValidationError

from library.api.books.models import Book


class Borrowing(models.Model):
    book_borrowed = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)

    def clean(self):
        if self.expected_return_date <= self.borrow_date:
            raise ValidationError("Expected return date must be after borrow date.")

        if self.actual_return_date <= self.borrow_date:
            raise ValidationError("Actual return date cannot be before borrow date.")