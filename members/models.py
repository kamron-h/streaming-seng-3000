from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
import streaming.models
from streaming import models


# Create your models here.

# Create an 'Account' profile automatically when registering new user***
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = streaming.models.Account(
            user=instance,
            # websites = [],
            # verified = False,
            # approved = False,
        )
        user_profile.save()


post_save.connect(create_profile, sender=User)
