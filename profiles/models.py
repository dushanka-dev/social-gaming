from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
# from django.urls import reverse
# from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    """User profile section"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    # user_picture = CloudinaryField(default='uploads/default-image.png')
    user_picture = models.ImageField(default='uploads/default.png', upload_to='uploads/', blank=True)
    # updated = models.DateTimeField(auto_now=True)
    profile_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user}-{self.profile_created}'
    
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)

class Friend(models.Model):
    """Upload User Profile picture to profile"""
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
