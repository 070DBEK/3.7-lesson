from django.contrib import admin
from .models import Food, Meal


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'calories')
    search_fields = ('name',)
    list_filter = ('calories',)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'meal_type')
    search_fields = ('user__username', 'meal_type')
    list_filter = ('date', 'meal_type')