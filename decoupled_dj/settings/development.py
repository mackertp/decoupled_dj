"""
This is a custom settings file specific to
the development setup. Use this while developing
the django project.


@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from .base import *


# --------------------------------------------------- #
# add custom dev settings
# --------------------------------------------------- #

INSTALLED_APPS += [
    "django_extensions"
]

CORS_ALLOW_ALL_ORIGINS = True