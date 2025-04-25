# serializers.py
from rest_framework import serializers
from .models import Workout, WorkoutExercise


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'exercise', 'name', 'sets', 'reps', 'weight']


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(source='workoutexercise_set', many=True)

    class Meta:
        model = Workout
        fields = ['id', 'date', 'duration', 'exercises']

    def create(self, validated_data):
        exercises_data = validated_data.pop('workoutexercise_set')
        workout = Workout.objects.create(**validated_data)
        for ex in exercises_data:
            WorkoutExercise.objects.create(
                workout=workout,
                exercise=ex['exercise'],
                sets=ex['sets'],
                reps=ex['reps'],
                weight=ex.get('weight')
            )
        return workout

    def update(self, instance, validated_data):
        exercises_data = validated_data.pop('workoutexercise_set', [])
        instance.date = validated_data.get('date', instance.date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        instance.workoutexercise_set.all().delete()
        for ex in exercises_data:
            WorkoutExercise.objects.create(
                workout=instance,
                exercise=ex['exercise'],
                sets=ex['sets'],
                reps=ex['reps'],
                weight=ex.get('weight')
            )
        return instance
