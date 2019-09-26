""" Transactions model"""

from django.db import models

from apps.common.models import CommonFieldsMixin


class Transaction(CommonFieldsMixin):
    """ Transaction model"""
    revenue_stream = models.CharField(max_length=255)
    income_stream = models.CharField(max_length=255)
    date_paid = models.CharField(max_length=255)
    receipt_number = models.CharField(max_length=255, unique=True)
    amount = models.FloatField()

    def __str__(self):
        return self.revenue_stream
    
    class Meta:
        abstract = False

