from rest_framework import viewsets
from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework.permissions import IsAuthenticated
from command.permissions import IsOwnerOrReadOnly
from command.pagination import CustomPagination


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class =  CustomPagination
    filterset_fields = ['date']
    search_fields = ['workout_exercises__exercise__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)