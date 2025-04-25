from django.db import models
from users.models import User

class HealthMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # A ForeignKey to the User model
    date = models.DateField()  # Date when the metrics were recorded
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # User's weight
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Optional body fat percentage
    blood_pressure_systolic = models.PositiveIntegerField(null=True, blank=True)  # Optional systolic blood pressure
    blood_pressure_diastolic = models.PositiveIntegerField(null=True, blank=True)  # Optional diastolic blood pressure
    heart_rate = models.PositiveIntegerField(null=True, blank=True)  # Optional heart rate

    def __str__(self):
        return f'{self.user.username} ({self.user.id}) health metrics on {self.date}'
