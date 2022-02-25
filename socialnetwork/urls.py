from django.urls import path
from . import views
from .views import PostsView, UserPostsView, EditPosts, DeletePost, Likes, CreateComment, EditComment

# URL Conf
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('myposts/', UserPostsView.as_view(), name='my-posts'),
    path('myposts/<int:pk>/likes', Likes.as_view(), name='likes'),
    path('comment/<int:pk>/', CreateComment.as_view(), name='comment'),
    path('editcomment/<int:pk>/', EditComment.as_view(), name='edit-comment'),
    path('editposts/<int:pk>/', EditPosts.as_view(), name='edit-posts'),
    path('deleteposts/<int:pk>/', DeletePost.as_view(), name='delete-posts'),
]
