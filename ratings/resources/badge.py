from rest_framework import serializers, viewsets

from ratings.models import Badge


class BadgeSerializer(serializers.ModelSerializer):
    """Сериализатор бейджей."""
    class Meta:
        model = Badge
        fields = '__all__'


class BadgeViewSet(viewsets.ModelViewSet):
    """Представление бейджей."""

    serializer_class = BadgeSerializer
    queryset = Badge.objects.filter(archive=False)
