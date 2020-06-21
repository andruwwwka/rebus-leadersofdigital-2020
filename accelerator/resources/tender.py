from django.contrib.contenttypes.models import ContentType
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

    def _calculate_votes_count(self, obj, interestingly):
        obj_type = ContentType.objects.get_for_model(obj)
        votes = Vote.objects.filter(
            content_type__pk=obj_type.id,
            object_id=obj.id,
            interestingly=interestingly
        )
        return votes.count()

    def get_like_count(self, obj):
        return self._calculate_votes_count(obj, True)

    def get_dislike_count(self, obj):
        return self._calculate_votes_count(obj, False)

    def get_comment_count(self, obj):
        return Comment.objects.filter(tender=obj).count()


class TenderViewSet(viewsets.ModelViewSet):
    """Представление идеи/предложения."""
    serializer_class = TenderSerializer
    queryset = Tender.objects.all()
