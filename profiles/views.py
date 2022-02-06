from django.shortcuts import render

# Create your views here.

def user_profile(request):
    """render user profile"""
    context = {
        'user': request.user
    }
    return render(request, 'userprofile.html', context)
