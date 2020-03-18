from django.urls import path

from ontecx.users.api import views as user_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "users"

urlpatterns = [
    path('api-token-auth/', TokenObtainPairView.as_view(), name="token_auth"),
    path('api-token-refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api-token-verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('signup/', user_views.UserCreateAPIView.as_view(), name="signup")
]
