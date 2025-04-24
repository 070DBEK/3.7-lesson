from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HealthMetrics
from .serializers import HealthMetricsSerializer


class HealthMetricsViewSet(viewsets.ModelViewSet):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    permission_classes = [IsAuthenticated]

    # Optional: You can add custom filters for start_date and end_date here if needed
    def get_queryset(self):
        queryset = HealthMetrics.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset
