from rest_framework import serializers
from .models import HealthMetrics


class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = [
            'id',
            'date',
            'weight',
            'body_fat_percentage',
            'blood_pressure_systolic',
            'blood_pressure_diastolic',
            'heart_rate',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        return representation
