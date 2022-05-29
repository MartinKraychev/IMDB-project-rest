from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Movies.user_auth.serializers import RegisterSerializer

UserModel = get_user_model()


class LoginView(ObtainAuthToken):
    """
    Login view with token authentication.
    """
    permission_classes = (
        AllowAny,
    )


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (
        AllowAny,
    )


class LogoutView(APIView):
    permission_classes = (
        IsAuthenticated,
    )

    @staticmethod
    def __perform_logout(request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({
            'message': 'User logged out'
        })

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)
