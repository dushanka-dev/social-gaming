from django.shortcuts import render
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

def user_profile(request):
    """User profile views with objects"""

    users_profile = UserProfile.objects.get(user=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=users_profile)
    form_update = False
    image_update = False

    if request.method == 'POST' and profile_form.is_valid():
        profile_form.save()
        form_update = True

    if request.FILES:
        profile_form.save()
        form_update = False
        image_update = True
        print("Image done!")

    context = {
        'users_profile': users_profile,
        'profile_form': profile_form,
        'form_update': form_update,
        'image_update': image_update,
    }
    return render(request, 'profiles/userprofile.html', context)
