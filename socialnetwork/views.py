from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
from django.views.generic import ListView
# from django.http import HttpResponse
from .models import Post
# from profiles.models import UserProfile


# def hello_social(response):
#     return render(response, 'base.html', {})

def home(response):
    """Landing page view"""
    return render(response, 'socialnetwork/landing.html', {})

# def post(response):
#     """Landing page view"""
#     return render(response, 'socialnetwork/posts.html', {})


class PostsView(ListView):
    """Display all posts"""
    model = Post
    template_name = 'socialnetwork/posts.html'
    ordering = ['-created_time']


class UserPostsView(ListView):
    """Display users posts"""
    model = Post
    template_name = 'socialnetwork/my-posts.html'
    ordering = ['-created_time']

    def get_queryset(self):
        """Display users posts"""
        users_posts = Post.objects.filter(author=self.request.user)
        return users_posts
        
