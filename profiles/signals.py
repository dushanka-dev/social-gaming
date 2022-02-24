from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, Friend

@receiver(post_save, sender=User)
def user_profile_created(sender, instance, created, **kwargs):
    """ Listen to user profile been created through signal """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Friend)
def add_friend_created(sender, instance, created, **kwargs):
    """ Listen to user profile been created through signal """

    send_friend_invite = instance.friend_sender
    recieve_friend_invite = instance.friend_receiver
    if instance.friend_status == 'accepted':
        send_friend_invite.friends.add(recieve_friend_invite.user)
        recieve_friend_invite.friends.add(send_friend_invite.user)
        send_friend_invite.save()
        recieve_friend_invite.save()
