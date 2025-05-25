from django.db import models


class Payment(models.Model):
    STATUS = (("pending", "paid"),("PENDING", "PAID"))
    TYPE = (("PAYMENT", "FINE"), ("payment", "fine"))

    status = models.CharField(max_length=7, choices=STATUS)
    type = models.CharField(max_length=7, choices=TYPE)
    borrowing_id = models.IntegerField()
    session_url = models.CharField(max_length=255)
    session_id = models.IntegerField()
    money_to_pay = models.DecimalField(max_digits=6, decimal_places=2)