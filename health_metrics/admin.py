from django.contrib import admin
from .models import HealthMetrics


@admin.register(HealthMetrics)
class HealthMetricsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'date', 'weight', 'body_fat_percentage',
        'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate'
    )
    list_filter = ('date',)
    search_fields = ('user__username', 'user__email')
