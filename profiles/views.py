from django.shortcuts import render
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

def user_profile(request):
    """User profile views with objects"""

    users_profile = UserProfile.objects.get(user=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=users_profile)

    context = {
        'users_profile': users_profile,
        'profile_form': profile_form,
    }
    return render(request, 'profiles/userprofile.html', context)
