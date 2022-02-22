from django.urls import path
from .views import UpdateProfile, FriendList

# URL Conf
urlpatterns = [
    path('profile/', UpdateProfile.as_view(), name='profile'),
    path('friends/', FriendList.as_view(), name='friends'),
    # path('<slug:slug>/', UpdateProfile.as_view(), name='profile'),
]
