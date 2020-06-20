from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля пользователя."""

    department = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'email',
            'last_name',
            'first_name',
            'patronymic',
            'photo',
            'phone',
            'internal_phone',
            'city',
            'birthday',
            'department',
            'position',
        )

    def get_department(self, obj):
        return obj.department.name

    def get_position(self, obj):
        return obj.position.post


class Profiles(APIView):
    """Информация профиля для личного кабинета."""
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
