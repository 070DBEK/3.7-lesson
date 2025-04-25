from django.urls import path
from .views import RegisterView, LogoutView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/signup/', RegisterView.as_view(), name='auth_register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('users/<str:username>/profile/', UserProfileView.as_view(), name='user-profile'),
]