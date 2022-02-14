from django.urls import path
from .views import UpdateProfile

# URL Conf
urlpatterns = [
    path('profile/', UpdateProfile.as_view(), name='profile'),
    # path('<slug:slug>/', UpdateProfile.as_view(), name='profile'),
]
