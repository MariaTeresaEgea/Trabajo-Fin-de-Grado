from rest_framework.permissions import BasePermission, SAFE_METHODS


def get_role(user):
    if not user or not user.is_authenticated:
        return None

    if user.is_superuser:
        return "ADMIN"

    profile = getattr(user, "profile", None)

    if not profile:
        return None

    return profile.role


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return get_role(request.user) == "ADMIN"


class IsAdminOrTeacherWrite(BasePermission):

    def has_permission(self, request, view):
        role = get_role(request.user)

        if role == "ADMIN":
            return True

        if request.method in SAFE_METHODS:
            return role in {
                "TEACHER",
                "STUDENT",
                "GUARDIAN",
            }

        return role == "TEACHER"


class IsAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.method in SAFE_METHODS
        )