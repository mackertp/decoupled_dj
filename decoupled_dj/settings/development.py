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

INSTALLED_APPS += ["django_extensions"]