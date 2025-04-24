from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Exercise.objects.all()
        user = self.request.user

        # Faqat joriy foydalanuvchining mashqlarini olish
        if user.is_authenticated:
            queryset = queryset.filter(user=user)

        # Optional: Sana bo'yicha filtr qo'shish (start_date, end_date)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset
