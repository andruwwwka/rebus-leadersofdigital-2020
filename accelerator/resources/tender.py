from rest_framework import serializers, viewsets

from ..models import Comment, Tender, Vote


class TenderSerializer(serializers.ModelSerializer):
    """Сериализатор идей/предложений"""
    owner = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

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
            'area',
            'like_count',
            'dislike_count',
            'comment_count',
        ]

    def get_owner(self, obj):
        return ' '.join([obj.owner.last_name, obj.owner.first_name, obj.owner.patronymic])

    def get_area(self, obj):
        return obj.area.name if obj.area else ''

    def like_count(self, obj):
        return Vote.objects.filter(content_object=obj, interestingly=True).count()

    def dislike_count(self, obj):
        return Vote.objects.filter(content_object=obj, interestingly=False).count()

    def omment_count(self, obj):
        return Comment.objects.filter(tender=obj).count()


class TenderViewSet(viewsets.ModelViewSet):
    """Представление идеи/предложения."""
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
