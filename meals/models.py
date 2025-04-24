from django.db import models
from django.conf import settings


class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack')
    ])
    foods = models.ManyToManyField(Food, through='MealFood')

    def __str__(self):
        return f'{self.user.username} {self.meal_type} on {self.date}'


class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.food.name} ({self.quantity} servings)"
