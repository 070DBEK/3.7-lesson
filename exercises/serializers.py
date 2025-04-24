from rest_framework import serializers
from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'category', 'calories_burned_per_hour']
