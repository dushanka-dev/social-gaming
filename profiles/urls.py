from django.urls import path
from .views import UpdateProfile, FriendList, Profiles

# URL Conf
urlpatterns = [
    path('profile/', UpdateProfile.as_view(), name='profile'),
    path('usersprofile/<int:pk>/', Profiles.as_view(), name='usersprofile'),
    path('friends/', FriendList.as_view(), name='friends'),
    # path('<slug:slug>/', UpdateProfile.as_view(), name='profile'),
]
