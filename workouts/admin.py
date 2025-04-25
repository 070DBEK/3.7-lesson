from django.contrib import admin
from .models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date')
    list_filter = ('date', 'user')
    search_fields = ('user__username',)

