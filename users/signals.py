from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    profile, _ = Profile.objects.get_or_create(
        user=instance
    )

    if instance.is_superuser and profile.role != Profile.Role.ADMIN:
        profile.role = Profile.Role.ADMIN
        profile.save(update_fields=["role"])