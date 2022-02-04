from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """User profile section"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    bio = models.TextField(max_length=500)
    country = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    user_picture = models.ImageField(default='default-pic.png', upload_to='uploads/')

class Friend(models.Model):
    """Upload User Profile picture to profile"""
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
