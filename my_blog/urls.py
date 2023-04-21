from django.urls import path, include
from rest_framework import routers
from .views import (
    AuthorViewSet,
    CategoryViewSet,
    CommentViewSet,
    PostViewSet,
    SubscriberViewSet,
    TagViewSet,
)

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('posts', PostViewSet)
router.register('subscribers', SubscriberViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
