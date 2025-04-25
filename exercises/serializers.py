from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'user', 'name', 'description', 'category', 'calories_burned_per_hour']
        read_only_fields = ['user']

    def create(self, validated_data):
        # Avtomatik tarzda foydalanuvchini qo‘shish
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
