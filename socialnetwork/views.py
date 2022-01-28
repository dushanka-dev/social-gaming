from django.shortcuts import render
from django.http import HttpResponse

def hello_social(request):
    return HttpResponse('Hello Social Page')
