from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Category, Comment, Post, Subscriber, Tag
from .serializers.AuthorSerializer import AuthorSerializer
from .serializers.CategorySerializer import CategorySerializer
from .serializers.CommentSerializer import CommentSerializer
from .serializers.PostSerializer import PostSerializer
from .serializers.SubscriberSerializer import SubscriberSerializer
from .serializers.TagSerializer import TagSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        author = self.get_object()
        posts = author.post_set.all()
        serializer = PostSerializer
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        category = self.get_object()
        posts = category.posts.all()
        serializer = PostSerializer
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comment_set.all()
        serializer = CommentSerializer
        return JsonResponse(serializer.data)


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        tag = self.get_object()
        posts = tag.posts.all()
        serializer = PostSerializer
        return Response(serializer.data)
