from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path('profile/', views.user_profile),
]
