from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet


router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
