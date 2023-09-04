from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bll.user_service import UserService
from .response_dto.registration_dto import Registration
from .serializers import LoginSerializer, RegistrationSerializer, RegistrationResponse
from .serializers import HelloSerializer
from socialnetworkapi.socialnetwork.serializers import UserSerializer, GroupSerializer


class LoginView(APIView):
    pass
    # def post(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         username = serializer.validated_data['username']
    #         password = serializer.validated_data['password']
    #
    #         user = authenticate(request, username=username, password=password)
    #
    #         if user is not None:
    #             login(request, user)
    #             return Response({'message': 'Authentication successful'})
    #         else:
    #             return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get('name')
            surname = request.data.get('surname')
            email = request.data.get('email')
            avatar = request.data.get('avatar')
            password = request.data.get('password')

            user = {
                'name': name,
                'surname': surname,
                'email': email,
                'avatar': avatar,
                'password': password
            }

            self.user_service.registration(user)

            return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
