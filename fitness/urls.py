from django.urls import path
from .views import (
    ExerciseListCreateView, ExerciseDetailView,
    WorkoutListCreateView, WorkoutDetailView,
    FoodListCreateView, FoodDetailView,
    MealListCreateView, MealDetailView,
    HealthMetricsListCreateView, HealthMetricsDetailView
)


urlpatterns = [
    path('exercises/', ExerciseListCreateView.as_view(), name='exercise-list-create'),
    path('exercises/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),

    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),

    path('foods/', FoodListCreateView.as_view(), name='food-list-create'),
    path('foods/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),

    path('meals/', MealListCreateView.as_view(), name='meal-list-create'),
    path('meals/<int:pk>/', MealDetailView.as_view(), name='meal-detail'),

    # Health  Endpoints
    path('health-metrics/', HealthMetricsListCreateView.as_view(), name='health-metrics-list-create'),
    path('health-metrics/<int:pk>/', HealthMetricsDetailView.as_view(), name='health-metrics-detail'),
]
