from django.shortcuts import render
from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse('Hello Landing Page')

def home(response):
    return render(response, 'landing.html', {})
