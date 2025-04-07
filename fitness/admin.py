from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise, Food, Meal, MealFood, HealthMetrics

# Inlines
class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

class MealFoodInline(admin.TabularInline):
    model = MealFood
    extra = 1

# Admin classes
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'duration')
    search_fields = ('user__username', 'date')
    inlines = [WorkoutExerciseInline]

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'calories_burned_per_hour')
    search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'carbs', 'fats')
    search_fields = ('name',)

class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meal_type')
    search_fields = ('user__username', 'date')
    inlines = [MealFoodInline]

class HealthMetricsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'weight', 'body_fat_percentage',
                    'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate')
    search_fields = ('user__username', 'date')

# Register your models here
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(HealthMetrics, HealthMetricsAdmin)
