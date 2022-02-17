from django.urls import path
from . import views
from .views import UserPostsView

# URL Conf
urlpatterns = [
    path('', views.home, name='home'),
    path('myposts/', UserPostsView.as_view(), name='my-post'),
]
