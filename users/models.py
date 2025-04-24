from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly Active'),
        ('moderately_active', 'Moderately Active'),
        ('very_active', 'Very Active'),
        ('extra_active', 'Extra Active'),
    ]
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_LEVEL_CHOICES)
    GOAL_CHOICES = [
        ('lose_weight', 'Lose Weight'),
        ('maintain_weight', 'Maintain Weight'),
        ('gain_weight', 'Gain Weight'),
        ('build_muscle', 'Build Muscle'),
    ]
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
