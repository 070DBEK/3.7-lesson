from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(
        choices=[('male', 'Male'), ('female', 'Female'),]
    )

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    activity_level = models.CharField(
        max_length=20,
        choices=[
            ('sedentary', 'Sedentary'), ('lightly_active', 'Lightly Active'),
            ('moderately_active', 'Moderately Active'), ('very_active', 'Very Active'),
            ('extra_active', 'Extra Active')
        ]
    )
    goal = models.CharField(
        max_length=20,
        choices=[
            ('lose_weight', 'Lose Weight'), ('maintain_weight', 'Maintain Weight'),
            ('gain_weight', 'Gain Weight'), ('build_muscle', 'Build Muscle')
        ]
    )