"""
These are the database models for interacting with the
billing application.

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.db import models
from django.conf import settings


# --------------------------------------------------- #
# defining the models
# --------------------------------------------------- #

class Invoice(models.Model):
    
    class State(models.TextChoices):
        PAID = "PAID"
        UNPAID = "UNPAID"
        CANCELLED = "CANCELLED"
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT
    )

    state = models.CharField(
        max_length=15, 
        choices=State.choices, 
        default=State.UNPAID
    )

    submitted_date = models.DateField()
    due_date = models.DateField()


class ItemLine(models.Model):
    invoice = models.ForeignKey(
        to=Invoice, on_delete=models.PROTECT, related_name="items"
    )
    quantity = models.IntegerField()
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    taxed = models.BooleanField()
