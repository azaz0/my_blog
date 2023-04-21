from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=False)
    categories = serializers.StringRelatedField(many=True, read_only=False)
    tags = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'date_posted', 'author', 'author_name', 'categories', 'tags')
