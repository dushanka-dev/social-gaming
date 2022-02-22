from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
# from django.views.generic.list import ListView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
# from django.views.generic.edit import UpdateView
from .models import UserProfile, Friend
# from .forms import ProfileForm

# Create your views here.

class FriendList(ListView):
    """Display all posts"""
    model = Friend
    template_name = 'profiles/friends.html'


class UpdateProfile(UpdateView):
    """Update Profile Model objects to display in template and POST data back to db"""
    model = UserProfile
    # form_class = ProfileForm
    fields = ['first_name', 'last_name', 'email', 'bio', 'favourite_game', 'user_picture']
    template_name = 'profiles/userprofile.html'
    success_url = 'profile'
    # success_message = 'Your Profile Updated Successfully!'

    def get_object(self, queryset=None):
        user_obj = get_object_or_404(UserProfile, user=self.request.user)
        return user_obj

    def form_valid(self, form):
        messages.success(self.request, 'Your Profile Updated Successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')
