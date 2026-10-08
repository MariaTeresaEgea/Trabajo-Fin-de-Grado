from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Profile, Teacher
from .permissions import IsAdmin
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    TeacherSerializer,
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.select_related(
        "profile"
    ).all().order_by(
        "last_name",
        "first_name"
    )

    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.select_related(
        "user"
    ).all()

    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]


class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.select_related(
        "user"
    ).all()

    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin]


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):

    user = request.user

    profile = getattr(
        user,
        "profile",
        None
    )

    return Response({
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "role": profile.role if profile else None,
        "role_display": (
            profile.get_role_display()
            if profile else None
        ),
    })