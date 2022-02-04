from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Create user profile models"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    bio = models.TextField(max_length=500)
    country = models.CharField(max_length=200, blank=True)
