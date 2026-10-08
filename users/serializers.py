from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, Teacher
from students.models import Student, Guardian


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=False
    )

    role = serializers.ChoiceField(
        choices=Profile.Role.choices,
        write_only=True,
        required=False
    )

    role_display = serializers.CharField(
        source="profile.get_role_display",
        read_only=True
    )

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "role",
            "role_display",
            "is_active",
        )

    def create(self, validated_data):

        role = validated_data.pop(
            "role",
            Profile.Role.STUDENT
        )

        password = validated_data.pop(
            "password",
            None
        )

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        Profile.objects.update_or_create(
            user=user,
            defaults={"role": role}
        )

        if role == Profile.Role.TEACHER:
            Teacher.objects.get_or_create(
                user=user
            )

        elif role == Profile.Role.GUARDIAN:
            Guardian.objects.get_or_create(
                user=user
            )

        elif role == Profile.Role.STUDENT:
            Student.objects.get_or_create(
                user=user,
                defaults={
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            )

        return user

    def update(self, instance, validated_data):

        role = validated_data.pop(
            "role",
            None
        )

        password = validated_data.pop(
            "password",
            None
        )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        if role:
            profile = instance.profile
            profile.role = role
            profile.save()

        return instance


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = (
            "id",
            "user",
            "user_name",
            "specialty",
            "bio",
            "active",
        )

    def get_user_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    