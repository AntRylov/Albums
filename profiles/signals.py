import logging
from .models import Profile

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

logger = logging.getLogger('album_logger')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            nickname=instance.username,
            email=instance.email
        )
        Profile.save(profile)
        logger.info(f"Profile for user {instance.username} has been created")