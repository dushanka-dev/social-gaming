from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post


# def hello_social(response):
#     return render(response, 'base.html', {})

def home(response):
    """Landing page view"""
    return render(response, 'socialnetwork/landing.html', {})

# def post(response):
#     """Landing page view"""
#     return render(response, 'socialnetwork/posts.html', {})


class UserPostsView(ListView):
    """Display users posts"""
    model = Post
    template_name = 'socialnetwork/posts.html'
