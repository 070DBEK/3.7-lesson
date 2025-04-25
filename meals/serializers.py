from rest_framework import serializers
from .models import Meal, Food, MealFood


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'calories', 'protein', 'carbs', 'fats']


class MealFoodSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), write_only=True, source='food')

    class Meta:
        model = MealFood
        fields = ['food', 'food_id', 'quantity']

class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerializer(many=True, source='meal_foods')

    class Meta:
        model = Meal
        fields = ['id', 'date', 'meal_type', 'foods']

    def create(self, validated_data):
        foods_data = validated_data.pop('meal_foods', [])
        meal = Meal.objects.create(**validated_data)

        for food_item in foods_data:
            MealFood.objects.create(
                meal=meal,
                food=food_item['food'],
                quantity=food_item['quantity']
            )
        return meal

    def update(self, instance, validated_data):
        foods_data = validated_data.pop('meal_foods', None)
        instance.date = validated_data.get('date', instance.date)
        instance.meal_type = validated_data.get('meal_type', instance.meal_type)
        instance.save()
        if foods_data is not None:
            instance.meal_foods.all().delete()
            for food_item in foods_data:
                MealFood.objects.create(
                    meal=instance,
                    food=food_item['food'],
                    quantity=food_item['quantity']
                )
        return instance