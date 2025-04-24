from rest_framework import serializers
from .models import Workout, WorkoutExercise
from exercises.models import Exercise


# Workout ichida ishlatiladigan Exercise serializer (custom fields bilan)
class WorkoutExerciseDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='exercise.id', read_only=True)
    name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'name', 'sets', 'reps', 'weight']


# Workout yaratish/yangilashda ishlatiladigan input serializer
class WorkoutExerciseInputSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())

    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight']


# Workout asosiy serializer
class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseDetailSerializer(source='workoutexercise_set', many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'date', 'duration', 'exercises']


# Workout yaratish va yangilash uchun serializer (POST/PUT)
class WorkoutCreateUpdateSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseInputSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['date', 'duration', 'exercises']

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(user=self.context['request'].user, **validated_data)
        for item in exercises_data:
            WorkoutExercise.objects.create(workout=workout, **item)
        return workout

    def update(self, instance, validated_data):
        exercises_data = validated_data.pop('exercises')
        instance.date = validated_data.get('date', instance.date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()

        # Old workout_exercises tozalaymiz
        instance.workoutexercise_set.all().delete()

        # Yangi workout_exercises yaratamiz
        for item in exercises_data:
            WorkoutExercise.objects.create(workout=instance, **item)

        return instance
