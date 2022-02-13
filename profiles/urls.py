from django.urls import path
from .views import ProfileView

# URL Conf
urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    # path('<slug:slug>/', UpdateProfile.as_view(), name='profile'),
]
