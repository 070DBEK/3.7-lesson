from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework.permissions import IsAuthenticated
from command.permissions import IsOwnerOrReadOnly
from command.pagination import CustomPagination


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class =  CustomPagination

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)
