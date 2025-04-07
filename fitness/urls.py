from rest_framework.routers import DefaultRouter
from .views import (
    ExerciseViewSet,
    WorkoutViewSet,
    MealViewSet,
    FoodViewSet,
    HealthMetricsViewSet
)


router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'meals', MealViewSet, basename='meal')
router.register(r'foods', FoodViewSet, basename='food')
router.register(r'health-metrics', HealthMetricsViewSet, basename='health-metrics')


urlpatterns = router.urls
