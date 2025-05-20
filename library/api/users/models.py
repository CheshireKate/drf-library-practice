from django.contrib.auth.models import AbstractUser
from django.db import models

from library.api.borrowings.models import Borrowing


class User(AbstractUser):
    borrowing = models.ForeignKey(Borrowing, on_delete=models.CASCADE, blank=True, null=True)