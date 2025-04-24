from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet

# Router yaratish
router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)

# URLConf
urlpatterns = [
    path('exercises/', include(router.urls)),
]
