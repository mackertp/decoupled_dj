"""
These are the url routes for the billing 
application

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.urls import path
from .views import Index
from .api.views import ClientList, InvoiceCreate


# --------------------------------------------------- #
# url routes
# --------------------------------------------------- #

app_name = "billing"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path(
        "api/clients/",
        ClientList.as_view(),
        name="client-list"),
    path(
        "api/invoices/",
        InvoiceCreate.as_view(),
        name="invoice-create"),
]

