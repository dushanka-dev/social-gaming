from django.shortcuts import render
from django.http import HttpResponse


# def hello_social(response):
#     return render(response, 'base.html', {})

def usersprofile(response):
    return render(response, 'userprofile.html', {})
