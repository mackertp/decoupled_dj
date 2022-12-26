"""
These are the url routes for the for the entire project

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.urls import path, include


# --------------------------------------------------- #
# url routes
# --------------------------------------------------- #

urlpatterns = [
    path(
        "billing/",
        include("billing.urls", namespace="billing")
    ),
]
