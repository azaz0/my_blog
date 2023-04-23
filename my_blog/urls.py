from django.urls import path, include
from django.contrib import admin
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
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'subscribers', SubscriberViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
