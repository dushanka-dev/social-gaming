from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path('home', views.home, name='home'),
]
