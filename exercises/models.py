from django.db import models


class Exercise(models.Model):
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    calories_burned_per_hour = models.PositiveIntegerField()

    def __str__(self):
        return self.name
