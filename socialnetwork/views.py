from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages
from .models import Post, Comment
from .forms import CreatePostForm, CommentsForm


def home(response):
    """Landing page view"""
    return render(response, 'socialnetwork/landing.html', {})


class PostsView(ListView):
    """Display all posts"""
    model = Post
    template_name = 'socialnetwork/posts.html'
    ordering = ['-created_time']


class Likes(View):
    """Display all posts"""

    def post(self, request, pk):
        """Display all posts"""
        posts = Post.objects.get(pk=pk)
        liked = False

        for like in posts.likes.all():
            if like == request.user:
                liked = True
                break
        else:
            posts.likes.add(request.user)

        if liked:
            posts.likes.remove(request.user)

        return HttpResponseRedirect(reverse('posts'))


class UserPostsView(View):
    """Display users posts"""

    def get(self, request):
        """Display users posts"""
        user_posts = Post.objects.filter(author=self.request.user).order_by('-post_date')
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
        form = CreatePostForm(request.POST, request.FILES)

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


class EditPosts(UpdateView):
    """Let users update posts"""

    model = Post
    # form_class = ProfileForm
    fields = ['title', 'body', 'post_picture']
    pk_url_kwarg = 'pk'
    template_name = 'socialnetwork/edit-posts.html'
    success_url = 'my-posts'
    ordering = ['-post_date']

    def form_valid(self, form):
        messages.success(self.request, 'Post edited Successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my-posts')


class DeletePost(DeleteView):
    """Delete selected user posts"""

    model = Post
    pk_url_kwarg = 'pk'
    template_name = 'socialnetwork/delete-post.html'
    success_url = 'my-posts'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted Successfully!')
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('my-posts')


class CreateComment(CreateView):
    """Let users create comment"""

    model = Comment
    form = CommentsForm
    fields = ['body']
    template_name = 'socialnetwork/comment.html'
    success_url = 'socialnetwork/posts.html'
    ordering = ['-comment_created']

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.posts = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.users = self.request.user
        
        messages.success(self.request, 'Comment created Successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts')


class EditComment(UpdateView):
    """Let users edit comments"""

    model = Comment
    # form_class = ProfileForm
    fields = ['body']
    pk_url_kwarg = 'pk'
    template_name = 'socialnetwork/edit-comment.html'
    success_url = 'posts'
    # ordering = ['-post_date']

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        # form.instance.posts = get_object_or_404(Post, pk=self.kwargs['pk'])
        # form.instance.users = self.request.user
        
        messages.success(self.request, 'Comment updated Successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts')


class DeleteComment(DeleteView):
    """Delete user comments"""

    model = Comment
    pk_url_kwarg = 'pk'
    template_name = 'socialnetwork/delete-comments.html'
    success_url = 'posts'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Comment deleted Successfully!')
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('posts')
