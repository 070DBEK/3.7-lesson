from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Workout.objects.all()
        user = self.request.user

        # Faqat joriy foydalanuvchining workout-larini olish
        if user.is_authenticated:
            queryset = queryset.filter(user=user)

        # Optional: Sana bo'yicha filtr qo'shish (start_date, end_date)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset
