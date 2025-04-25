from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HealthMetrics
from .serializers import HealthMetricsSerializer
from command.permissions import IsOwnerOrReadOnly
from command.pagination import CustomPagination
from rest_framework.filters import OrderingFilter


class HealthMetricsViewSet(viewsets.ModelViewSet):
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['date', 'weight', 'body_fat_percentage']

    def get_queryset(self):
        """
        Optionally filters the queryset based on the start_date and end_date query parameters.
        """
        queryset = HealthMetrics.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset

    def perform_create(self, serializer):
        """
        Custom save method to associate the logged-in user with the health metric.
        """
        serializer.save(user=self.request.user)