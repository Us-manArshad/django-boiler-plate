from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import SignupSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class UsersViewSet(ReadOnlyModelViewSet):

    def get_queryset(self):
        queryset = super(UsersViewSet, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)

    serializer_class = UserSerializer
    queryset = User.objects.all()
