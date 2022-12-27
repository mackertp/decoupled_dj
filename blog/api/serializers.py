"""

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

from blog.models import Blog
from rest_framework import serializers


# --------------------------------------------------- #
# serializers
# --------------------------------------------------- #

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "title",
            "body",
            "created_at",
            "status",
            "id"
        ]
