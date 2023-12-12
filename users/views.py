from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from .serializers import (
    UserRegistrationSerializer,
    UserInformationSerializer,
    ChangePasswordSerializer,
    UpdateProfileSerializer
)
from rest_framework.permissions import IsAuthenticated
from utils.confirmation_email_utils import send_confirmation_email
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            send_confirmation_email(serializer.instance)
            return Response({"message": "Registration successful. A confirmation link has been sent to your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmEmailView(APIView):
    """
    Confirm Email View.

    """

    def get(self, request):
        token = request.GET.get('token', None)
        if token:
            try:
                access_token = AccessToken(token)
                user = User.objects.get(id=access_token['user_id'])
                user.is_active = True
                user.save()
                return Response({'message': 'Email has been successfully confirmed.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': 'Invalid confirmation token.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Token is missing.'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    User Profile View.

    This view allows authenticated users to retrieve their profile information.

    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserInformationSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    """
    Change Password View.

    """
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            confirm_new_password = serializer.validated_data['confirm_new_password']

            user = request.user

            if not user.check_password(old_password):
                return Response({'incorrect_password_error': 'Old password is incorrect.'},
                                status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_new_password:
                return Response({'not_match_error': 'New passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdateView(UpdateAPIView):
    """
    Profile Update View.

    """
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if 'email' in request.data and instance.email != request.data['email']:
            instance.is_active = False
            send_confirmation_email(serializer.instance)
        return Response(serializer.data)


