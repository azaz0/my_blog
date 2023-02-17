from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts_view'),
    path('posts/<int:post_id>', views.post, name='single_post_view'),
    path('posts/<str:post_id>', views.post, name='single_post_view'),
    path('posts/<str:post_name>', views.post, name='single_post_view'),
]
