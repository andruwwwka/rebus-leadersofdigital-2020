from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля пользователя."""

    department = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    birthday = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Profile
        fields = (
            'id',
            'email',
            'last_name',
            'first_name',
            'patronymic',
            'photo',
            'little_avatar',
            'phone',
            'internal_phone',
            'city',
            'birthday',
            'department',
            'position',
        )

    def get_department(self, obj):
        """Получение названия подразделения, в котором работает сотрудник."""
        return obj.department.name

    def get_position(self, obj):
        """Получение наименования должности сотрудника."""
        return obj.position.post


class Profiles(APIView):
    """Информация профиля для личного кабинета."""
    serializer_class = ProfileSerializer

    def get(self, request):
        """Получение профиля пользователя."""
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
