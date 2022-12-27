"""
These are the url routes for the blog app

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.urls import path
from .api.views import BlogList, BlogDetail


# --------------------------------------------------- #
# url routes
# --------------------------------------------------- #

app_name = "blog"

urlpatterns = [
    path(
        "api/posts/",
        BlogList.as_view(),
        name="list"),
    path(
        "api/posts/<int:pk>",
        BlogDetail.as_view(),
        name="detail"),
]

