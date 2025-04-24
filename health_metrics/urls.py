from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthMetricsViewSet

router = DefaultRouter()
router.register(r'health-metrics', HealthMetricsViewSet)

urlpatterns = [
    path('health-metrics/', include(router.urls)),
]
