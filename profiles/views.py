from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
# from django.views.generic.edit import UpdateView
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

class UpdateProfile(UpdateView):
    """Update Profile Model objects to display in template and POST data back to db"""
    model = UserProfile
    # form_class = ProfileForm
    fields = ['first_name', 'last_name', 'email', 'bio', 'favourite_game']
    template_name = 'profiles/userprofile.html'
    success_url = 'profile'

    def get_object(self, queryset=None):
        obj = obj = get_object_or_404(UserProfile, user=self.request.user)
        return obj

    def get_success_url(self):
        return reverse('profile')

