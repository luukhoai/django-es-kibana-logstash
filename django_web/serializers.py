from rest_framework.serializers import ModelSerializer
from .models import BlogPost


class BlogpostSerializer(ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('id', 'author', 'title', 'text', 'created_at', 'updated_at')