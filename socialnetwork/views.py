from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
# from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from .forms import CreatePostForm
# from profiles.models import UserProfile


def home(response):
    """Landing page view"""
    return render(response, 'socialnetwork/landing.html', {})


class PostsView(ListView):
    """Display all posts"""
    model = Post
    template_name = 'socialnetwork/posts.html'
    ordering = ['-created_time']


# class UserPostsView(ListView):
#     """Display users posts"""
#     model = Post
#     template_name = 'socialnetwork/my-posts.html'
#     ordering = ['-created_time']

#     def get_queryset(self):
#         """Display users posts"""
#         user_posts = Post.objects.filter(author=self.request.user)
#         return user_posts

class UserPostsView(View):
    """Display users posts"""

    def get(self, request, *args, **kwargs):
        """Display users posts"""
        user_posts = Post.objects.filter(author=self.request.user)
        form = CreatePostForm()

        context = {
            'user_post_list': user_posts,
            'form': form,
        }

        return render(request, 'socialnetwork/my-posts.html', context)

    def post(self, request):
        """Display users posts"""
        posts = Post.objects.filter(author=self.request.user)
        new_posts = posts.order_by('-created_time')
        form = CreatePostForm(request.POST)

        if form.is_valid():
            users_new_post = form.save(commit=False)
            users_new_post.author = self.request.user
            users_new_post.save()
            messages.add_message(request, messages.INFO, 'Post Created Successfully!')

        context = {
            'user_post_list': new_posts,
            'form': form,
        }

        return render(request, 'socialnetwork/my-posts.html', context)

