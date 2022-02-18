from django.urls import path
from . import views
from .views import PostsView, UserPostsView

# URL Conf
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('myposts/', UserPostsView.as_view(), name='my-posts'),
    # path('myposts/', CreatePost.as_view(), name='my-posts'),
]
