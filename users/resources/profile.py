from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from organization.models import Department
from users.models import Position, Profile


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор Департамента"""
    class Meta:
        model = Department
        fields = ['name']


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор Должностей"""
    class Meta:
        model = Position
        fields = ['post']


class ProfileSerializer(serializers.Serializer):
    """Сериализатор профиля пользователя"""
    email = serializers.EmailField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    patronymic = serializers.CharField()
    photo = serializers.FileField()
    phone = serializers.CharField()
    internal_phone = serializers.CharField()
    city = serializers.CharField()
    birthday = serializers.DateField()
    department = DepartmentSerializer()
    position = PositionSerializer()


class Profiles(APIView):
    """Работа с профилем"""
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
