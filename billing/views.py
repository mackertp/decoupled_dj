"""
These are the defined views for the billing 
application

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# --------------------------------------------------- #
# views
# --------------------------------------------------- #

class Index(LoginRequiredMixin, TemplateView):
    template_name = "billing/index.html"

