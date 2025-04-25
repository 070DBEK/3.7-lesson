from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet

# Router yaratish
router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet)

# URLConf
urlpatterns = [
    path('', include(router.urls)),
]
