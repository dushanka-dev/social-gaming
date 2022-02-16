from django.shortcuts import render
from django.http import HttpResponse


# def hello_social(response):
#     return render(response, 'base.html', {})

def home(response):
    return render(response, 'socialnetwork/landing.html', {})

def post(response):
    return render(response, 'socialnetwork/posts.html', {})
