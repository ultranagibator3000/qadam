from rest_framework import serializers

from apps.news.models import News


class NewsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["title", "body", "image"]


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "image", "created_at"]


class NewsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["title", "body", "image", "created_at", "updated_at"]
