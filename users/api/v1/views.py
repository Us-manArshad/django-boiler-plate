from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialConnectView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.api.v1.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class FacebookLoginAPI(SocialLoginView):
    authentication_classes = []
    permission_classes = []
    adapter_class = FacebookOAuth2Adapter


class GoogleLoginAPI(SocialLoginView):
    authentication_classes = []
    permission_classes = []
    adapter_class = GoogleOAuth2Adapter


class FacebookLoginConnectAPI(SocialConnectView):
    authentication_classes = []
    permission_classes = []
    adapter_class = FacebookOAuth2Adapter


class GoogleLoginConnectAPI(SocialConnectView):
    authentication_classes = []
    permission_classes = []
    adapter_class = GoogleOAuth2Adapter
