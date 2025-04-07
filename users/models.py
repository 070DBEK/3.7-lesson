from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    # username = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):

    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly_active'),
        ('moderately_active', 'Moderately_active'),
        ('very_active', 'Very_active'),
        ('extra_active', 'Extra_active'),
    ]

    GOAL_CHOICES = [
        ('lose_weight', 'Lose_weight'),
        ('maintain_weight', 'Maintain_weight'),
        ('gain_weight', 'Gain_weight'),
        ('build_muscle', 'Build_muscle')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    activity_level = models.CharField(max_length=100, choices=ACTIVITY_LEVEL_CHOICES)
    goal = models.CharField(max_length=100, choices=GOAL_CHOICES)

    def __str__(self):
        return f'{self.user} profile'