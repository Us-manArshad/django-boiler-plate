from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.api.v1.viewsets import SignupViewSet, UsersViewSet
from users.api.v1.views import *


router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("users", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/',
         CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Social Login
    path("login/social/google/", GoogleLoginAPI.as_view(), name="google_login"),
    path("login/social/google/connect/", GoogleLoginConnectAPI.as_view(), name="google_login_connect"),
    path("login/social/facebook/", FacebookLoginAPI.as_view(), name="facebook_login"),
    path("login/social/facebook/connect/", FacebookLoginConnectAPI.as_view(), name="facebook_login_connect"),
]
