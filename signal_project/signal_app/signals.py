from django.contrib.auth.models import User
from signal_app.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('****************')
        print('Profile created!')
        print('****************')


# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created is False:
        instance.profile.save()
        print('****************')
        print('Profile Updated!')
        print('****************')


# post_save.connect(update_profile, sender=User)
