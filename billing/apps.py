"""
Configure the application to be used in django

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.apps import AppConfig


# --------------------------------------------------- #
# config
# --------------------------------------------------- #

class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing'
