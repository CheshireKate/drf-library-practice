from django.db import models
from django.db.models import ManyToManyField

class Author(models.Model):
    last_name = models.CharField(max_length=255, primary_key=True, index=True)
    first_name = models.CharField(max_length=255, black=True, null=True)


class Book(models.Model):
    COVER_TYPE = (
        ("hard", "Hard"),
        ("soft", "Soft")
    )


    title = models.CharField(max_length=255, primary_key=True, index=True)
    author = ManyToManyField(Author)
    cover = models.CharField(max_length=10, choices=COVER_TYPE, null=True)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=6, decimal_places=2)