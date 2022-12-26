"""
This file is used so that the custom user model application
can be included inside of the django settings.

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.apps import AppConfig


# --------------------------------------------------- #
# application config for custom users
# --------------------------------------------------- #

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
