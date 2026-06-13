from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    age = models.PositiveIntegerField(
        default=18
    )

    weight = models.FloatField(
        default=70
    )

    height = models.FloatField(
        default=170
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default="Male"
    )

    daily_goal = models.PositiveIntegerField(
        default=2200
    )

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_profile(
    sender,
    instance,
    created,
    **kwargs
):

    if created:

        Profile.objects.create(
            user=instance
        )    