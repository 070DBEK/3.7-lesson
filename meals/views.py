from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Meal, Food
from .serializers import MealSerializer, CreateMealSerializer, FoodSerializer, FoodUpdateSerializer

# Food uchun ViewSet
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Food.objects.all()
        # Agar kerak bo'lsa, maxsus filtrlashlar qo'shish mumkin
        return queryset

# Meal uchun ViewSet
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # Agar POST request bo'lsa, CreateMealSerializer ishlatiladi
        if self.action == 'create':
            return CreateMealSerializer
        return MealSerializer

    def get_queryset(self):
        # Foydalanuvchining meal-larini olish
        user = self.request.user
        return Meal.objects.filter(user=user)

    def perform_create(self, serializer):
        # Meal yaratishda foydalanuvchi bilan bog'lash
        serializer.save(user=self.request.user)
