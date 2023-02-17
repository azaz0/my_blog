from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-starting-page'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<int:post_id>', views.post_detail, name='post-detail-page'),
]
