from rest_framework import serializers

from .models import Blog



class BlogsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'description',
            'category',
            'image_url',
        )