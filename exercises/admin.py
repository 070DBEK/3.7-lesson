from django.contrib import admin
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'category', 'calories_burned_per_hour')
    list_filter = ('category', 'user')
    search_fields = ('name', 'description')
    fields = ('user', 'name', 'description', 'category', 'calories_burned_per_hour')