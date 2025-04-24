from rest_framework import serializers
from .models import Food, Meal, MealFood

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'protein', 'carbs', 'fats']


class MealFoodSerializer(serializers.ModelSerializer):
    food = FoodSerializer()  # Nested serializer to display food details

    class Meta:
        model = MealFood
        fields = ['food', 'quantity']


class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerializer(many=True)  # List of foods with their quantity

    class Meta:
        model = Meal
        fields = ['id', 'user', 'date', 'meal_type', 'foods']


class CreateMealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerializer(many=True)  # List of foods and their quantity

    class Meta:
        model = Meal
        fields = ['id', 'user', 'date', 'meal_type', 'foods']

    def create(self, validated_data):
        foods_data = validated_data.pop('foods')
        meal = Meal.objects.create(**validated_data)
        for food_data in foods_data:
            MealFood.objects.create(meal=meal, **food_data)
        return meal


class FoodUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'protein', 'carbs', 'fats']
