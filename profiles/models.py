from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    """User profile section"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    favourite_game = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, null=True)
    # user_picture = CloudinaryField(default='uploads/default-image.png')
    user_picture = models.ImageField(default='uploads/default.png', upload_to='uploads/', blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    updated = models.DateTimeField(auto_now=True)
    profile_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user}-{self.profile_created}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Friend(models.Model):
    """Upload User Profile picture to profile"""

    friend_sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friend_sender', default=None)
    friend_receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='friend_receiver', default=None)
    friend_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=None)
    friend_created = models.DateField(default=timezone.now)
    friend_updated = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.friend_sender}-{self.friend_receiver}-{self.friend_status}'
