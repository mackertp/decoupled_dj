"""
This is a custom settings file specific to
the production setup for our project.

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from .base import *


# --------------------------------------------------- #
# add custom dev settings
# --------------------------------------------------- #

SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
STATIC_ROOT = env("STATIC_ROOT")

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# --------------------------------------------------- #
# additional apps for audit logging
# --------------------------------------------------- #

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]
}

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS",default=[])

