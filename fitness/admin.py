from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise, Food, Meal, MealFood, HealthMetrics


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'calories_burned_per_hour')
    search_fields = ('name', 'category')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'duration')
    list_filter = ('date',)
    search_fields = ('user__username',)


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'sets', 'reps', 'weight')
    list_filter = ('workout', 'exercise')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'carbs', 'fats')
    search_fields = ('name',)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meal_type')
    list_filter = ('meal_type', 'date')
    search_fields = ('user__username',)


@admin.register(MealFood)
class MealFoodAdmin(admin.ModelAdmin):
    list_display = ('meal', 'food', 'quantity')
    list_filter = ('meal', 'food')


@admin.register(HealthMetrics)
class HealthMetricsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'weight', 'body_fat_percentage', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate')
    list_filter = ('date', 'user')
