from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    LogoutAndBlacklistRefreshTokenForUserView, 
    ObtainTokenPairWithPointsView,
    CurrentUserView,
    UserCreate,
    CurrentUserView,
)

urlpatterns = [
    path('create/', UserCreate.as_view(), name='create_user'),
    path('token/obtain/', ObtainTokenPairWithPointsView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),

    path('current_user/', CurrentUserView.as_view(), name='current_user'),
]
