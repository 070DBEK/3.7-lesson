from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    SignUpView,
    CustomTokenObtainPairView,
    UserProfileView
)


urlpatterns = [
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/profile/', UserProfileView.as_view(), name='user-profile'),
]

