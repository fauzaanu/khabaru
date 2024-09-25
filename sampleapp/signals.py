"""
Signal to catch user creation and if its the only user in the database, make it a superuser
"""

from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def make_user_superuser(sender, instance, created, **kwargs):
    if created and User.objects.count() == 1:
        instance.is_superuser = True
        instance.is_staff = True
        instance.save()
        print("User is now a superuser")
    else:
        print("User is not a superuser")


@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    "if there is no superuser, lets make the first user a superuser"
    if User.objects.filter(
            is_superuser=True
    ).count() == 0 and User.objects.count() > 0:
        # get the first user
        user = User.objects.first()
        user.is_superuser = True
        user.is_staff = True
        user.save()

        print("User is now a superuser")
