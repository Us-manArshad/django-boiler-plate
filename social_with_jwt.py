class Googlelogin(SocialLoginView):
    adapter_class = google_views.GoogleOAuth2Adapter
    client_class = OAuth2Client
    def get_response(self):
        # Call the parent get_response() method for authentication
        response = super().get_response()
        if self.request.user.is_authenticated:
            # Generate JWT token
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            payload = jwt_payload_handler(self.request.user)
            token = jwt.encode(payload, None, None)
            # Add the token to the response
            response.data['access_token'] = token
