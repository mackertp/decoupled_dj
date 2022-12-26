"""
Setting up a custom user model

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


# --------------------------------------------------- #
# models
# --------------------------------------------------- #

class User(AbstractUser):
    name = CharField(blank=True, max_length=100)

    def __str__(self):
        return self.email