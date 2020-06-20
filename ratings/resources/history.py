from rest_framework import serializers, viewsets

from ratings.models import History


class HistorySerializer(serializers.ModelSerializer):
    """Сериализатор истории наград/бейджей"""
    class Meta:
        model = History
        fields = '__all__'


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление истории наград/бейджей"""

    serializer_class = HistorySerializer
    queryset = History.objects.all()

