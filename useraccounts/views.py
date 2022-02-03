from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_profile(request):
    context = {
        'user': request.user
    }

    return render(request, 'userprofile.html', context)
