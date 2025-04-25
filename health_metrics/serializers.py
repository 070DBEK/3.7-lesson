from rest_framework import serializers
from .models import HealthMetrics
from users.models import User


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

    # Response formatni moslashtirish
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Qo'shimcha tahrirlar qilish mumkin, masalan, sana formatlash
        representation['date'] = instance.date.strftime('%Y-%m-%d')  # Sana formatlash
        return representation

    # To'liq Response ni moslashtirish uchun `to_representation` metodini ishlatamiz.
