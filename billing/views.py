"""
These are the defined views for the billing 
application

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.views.generic import TemplateView


# --------------------------------------------------- #
# views
# --------------------------------------------------- #

class Index(TemplateView):
    template_name = "billing/index.html"

