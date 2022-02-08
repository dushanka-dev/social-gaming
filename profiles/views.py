from django.shortcuts import render
from .models import UserProfile

# Create your views here.

def user_profile(request):
    """User profile views with objects"""

    users_profile = UserProfile.objects.get(user=request.user)
    context = {
        'users_profile': users_profile,
    }
    return render(request, 'profiles/userprofile.html', context)
