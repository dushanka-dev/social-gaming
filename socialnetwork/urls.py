from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post, name='post'),
]
