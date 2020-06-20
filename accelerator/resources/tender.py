from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

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
        return obj.area.name


class TenderViewSet(viewsets.ModelViewSet):
    """Представление идеи/предложения"""
    permission_classes = [permissions.AllowAny]

    @action(detail=True)
    def list(self, request, *args, **kwargs):
        tenders = Tender.objects.all()
        ser = TenderSerializer(tenders, many=True)
        return Response(ser.data)
