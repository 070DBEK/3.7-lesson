from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exercise
from .serializers import ExerciseSerializer
from command.permissions import IsOwnerOrReadOnly  # sen yozgan permission

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Faqat joriy foydalanuvchining mashqlari
        return Exercise.objects.filter(user=self.request.user)
