from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Meal, Food
from .serializers import MealSerializer, FoodSerializer
from command.permissions import IsOwnerOrReadOnly


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Food.objects.all()
        return queryset


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        date = self.request.query_params.get('date', None)
        meal_type = self.request.query_params.get('meal_type', None)
        queryset = Meal.objects.filter(user=user)
        if date:
            queryset = queryset.filter(date=date)
        if meal_type:
            queryset = queryset.filter(meal_type=meal_type)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

