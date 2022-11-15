from rest_framework import serializers

from apps.blogs.models import Blog, BlogAssets


class BlogAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogAssets
        fields = ["file"]


class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "body"]


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "author", "title", "updated_at"]


class BlogRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["author", "title", "body", "created_at", "updated_at"]
