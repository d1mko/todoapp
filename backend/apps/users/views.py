from django.contrib import auth
from django.contrib.auth import get_user_model
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication

from .serializers import RegisterSerializer

User = get_user_model()


class Whoami(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'isAuthenticated': false})

        return Response({'email': request.user.email})


class CheckAuthenticatedView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            return Response({'isAuthenticated': 0})

        return Response({'isAuthenticated': 1})


class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        response = Response({'success': 'CSRF cookie set'})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Expose-Headers"] = ['Content-Type', 'X-CSRFToken', 'Set-Cookie']
        response['X-CSRFToken'] = get_token(request)
        return response


@method_decorator(ensure_csrf_cookie, name='dispatch')
class RegisterView(generics.CreateAPIView):
    model = User
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer


@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']

        try:
            user = auth.authenticate(username=email, password=password)

            if user is not None:
                auth.login(request, user)
                return Response({'success': 'User authenticated'})

            return Response({'error': 'Error Authenticating'},
                            status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error': 'Something went wrong when logging in'},
                            status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success': 'Logged out'})
        except:
            return Response({'error': 'Something went wrong when logging out'})
