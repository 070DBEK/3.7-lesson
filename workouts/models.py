from django.db import models
from django.conf import settings
from exercises.models import Exercise


class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
