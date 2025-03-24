from django.db import models
from  users.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=[('cardio', 'Cardio'), ('strength', 'Strength'), ('flexibility', 'Flexibility'), ('balance', 'Balance')]
    )
    calories_burned_per_hour = models.PositiveIntegerField()


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(
        max_length=20,
        choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')]
    )
    foods = models.ManyToManyField(Food, through='MealFood')


class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)


class HealthMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blood_pressure_systolic = models.PositiveIntegerField(null=True, blank=True)
    blood_pressure_diastolic = models.PositiveIntegerField(null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)
