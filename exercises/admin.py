from django.contrib import admin
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date')
    list_filter = ('date',)
    search_fields = ('user__username',)
