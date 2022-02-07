from django.shortcuts import render
from .models import UserProfile

# Create your views here.

def user_profile(request):
    """User profile views with objects"""

    user_obj = UserProfile.objects.get(user=request.user)
    context = {
        'user_obj': user_obj,
    }
    return render(request, 'profiles/userprofile.html', context)
