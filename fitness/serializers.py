from rest_framework import serializers
from .models import (
    Exercise, Workout, WorkoutExercise, Food, Meal, MealFood, HealthMetrics
)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'category', 'calories_burned_per_hour']


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ['id', 'workout', 'exercise', 'sets', 'reps', 'weight']

    def validate_sets(self, value):
        if value < 1:
            raise serializers.ValidationError("Sets must be at least 1.")
        return value

    def validate_reps(self, value):
        if value < 1:
            raise serializers.ValidationError("Reps must be at least 1.")
        return value

    def validate_weight(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Weight cannot be negative.")
        return value


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'date', 'duration', 'exercises']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'protein', 'carbs', 'fats']


class MealFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealFood
        fields = ['id', 'meal', 'food', 'quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value


class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'user', 'date', 'meal_type', 'foods']


class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = [
            'id', 'user', 'date', 'weight', 'body_fat_percentage',
            'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate'
        ]

    def validate_weight(self, value):
        if value <= 0:
            raise serializers.ValidationError("Weight must be greater than zero.")
        return value

    def validate_body_fat_percentage(self, value):
        if value is not None and (value < 0 or value > 100):
            raise serializers.ValidationError("Body fat percentage must be between 0 and 100.")
        return value

    def validate_blood_pressure_systolic(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Systolic blood pressure must be positive.")
        return value

    def validate_blood_pressure_diastolic(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Diastolic blood pressure must be positive.")
        return value

    def validate_heart_rate(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Heart rate must be positive.")
        return value