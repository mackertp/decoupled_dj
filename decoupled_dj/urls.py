"""
These are the url routes for the for the entire project

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from django.urls import path, include
from django.contrib import admin
from django.conf import settings

# --------------------------------------------------- #
# url routes
# --------------------------------------------------- #

urlpatterns = [
    path(
        "auth/", 
        include("login.urls", namespace="auth")
    ),
    path(
        "billing/",
        include("billing.urls", namespace="billing")
    ),
    path(
        "blog/",
        include("blog.urls", namespace="blog")
    ),
]

if settings.DEBUG:
    urlpatterns = [
        path("admin/", admin.site.urls),
    ] + urlpatterns

if not settings.DEBUG:
    urlpatterns = [
        path("administration@20/", admin.site.urls),
    ] + urlpatterns

