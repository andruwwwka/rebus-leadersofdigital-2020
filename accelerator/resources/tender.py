from rest_framework import serializers, viewsets

from accelerator.models import Tender


class TenderSerializer(serializers.ModelSerializer):
    """Сериализатор идей/предложений"""
    owner = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()

    class Meta:
        model = Tender
        fields = [
            'id',
            'caption',
            'description',
            'presentation',
            'status',
            'owner',
            'tender_type',
            'area'
        ]

    def get_owner(self, obj):
        return ' '.join([obj.owner.last_name, obj.owner.first_name, obj.owner.patronymic])

    def get_area(self, obj):
        return obj.area.name or ''


class TenderViewSet(viewsets.ModelViewSet):
    """Представление идеи/предложения."""
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
