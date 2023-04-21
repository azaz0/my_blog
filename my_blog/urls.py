from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'subscribers', views.SubscriberViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
