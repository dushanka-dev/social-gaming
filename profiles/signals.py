from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def user_profile_created(sender, instance, created, **kwargs):
    """ Listen to user profile been created through signal """
    if created:
        UserProfile.objects.create(user=instance)
