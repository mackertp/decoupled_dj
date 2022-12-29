"""
Sets up an index to link the vue application with 
a standard Django template view

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

