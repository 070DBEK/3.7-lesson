from rest_framework import viewsets, permissions
from .models import Workout
from .serializers import WorkoutSerializer
from command.permissions import IsOwnerOrReadOnly


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filterset_fields = ['date']
    search_fields = ['workout_exercises__exercise__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)