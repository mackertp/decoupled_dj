"""
These are the api views for working with the 
billing application

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from .serializers import InvoiceSerializer
from .serializers import UserSerializer, User
from rest_framework.generics import CreateAPIView, ListAPIView


# --------------------------------------------------- #
# views
# --------------------------------------------------- #

class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer

