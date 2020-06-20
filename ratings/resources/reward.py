from rest_framework import serializers, viewsets

from ratings.models import Reward


class RewardSerializer(serializers.ModelSerializer):
    """Сериализатор наград"""
    class Meta:
        model = Reward
        fields = '__all__'


class RewardViewSet(viewsets.ModelViewSet):
    """Представление наград"""

    serializer_class = RewardSerializer
    queryset = Reward.objects.filter(archive=False)
