from django.urls import path
from . import views
from .views import PostsView, UserPostsView, EditPosts, DeletePost

# URL Conf
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('myposts/', UserPostsView.as_view(), name='my-posts'),
    path('editposts/<slug:slug>/', EditPosts.as_view(), name='edit-posts'),
    path('deleteposts/<slug:slug>/', DeletePost.as_view(), name='delete-posts'),
    # path('myposts/', CreatePost.as_view(), name='my-posts'),
]
