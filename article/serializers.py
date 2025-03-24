from rest_framework import serializers
from .models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=False)

    class Meta:
        model = Blog
        fields = ["categories", "title", "created_time", "content"]
