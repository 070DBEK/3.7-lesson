from django.urls import path
from .views import RegisterView, LoginAPIView, LogoutAPIView, UserProfileView


urlpatterns = [
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/logout/', LogoutAPIView.as_view(), name='logout'),
    path('users/profile/', UserProfileView.as_view(), name='profile'),
]
