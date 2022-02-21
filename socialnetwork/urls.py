from django.urls import path
from . import views
from .views import PostsView, UserPostsView, EditPosts, DeletePost

# URL Conf
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('myposts/', UserPostsView.as_view(), name='my-posts'),
    path('editposts/<int:pk>/', EditPosts.as_view(), name='edit-posts'),
    path('deleteposts/<int:pk>/', DeletePost.as_view(), name='delete-posts'),
]
