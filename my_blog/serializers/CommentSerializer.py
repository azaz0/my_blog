from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'email', 'body', 'date_posted', 'post')
