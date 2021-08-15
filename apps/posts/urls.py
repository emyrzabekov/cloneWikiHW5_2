from django.urls import path
from .views import index, posts_list, post_detail

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:pk>/', posts_list, name='posts'),
    path('posts/post_detail/<int:pk>/', post_detail, name='post_detail'),
]