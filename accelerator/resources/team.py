from rest_framework import serializers, viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet

from accelerator.models import Team
from users.models import Profile


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'patronymic']


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор команды"""
    leader = serializers.SerializerMethodField()
    expert = serializers.SerializerMethodField()
    idea = serializers.SerializerMethodField()
    partner = PartnerSerializer(many=True, read_only=False)

    class Meta:
        model = Team
        fields = [
            'id',
            'caption',
            'leader',
            'expert',
            'partner',
            'idea',
        ]

    def get_leader(self, obj):
        return ' '.join([obj.leader.last_name, obj.leader.first_name, obj.leader.patronymic])

    def get_expert(self, obj):
        return ' '.join([obj.expert.last_name, obj.expert.first_name, obj.expert.patronymic])

    def get_partner(self, obj):
        return ' '.join([obj.partner.last_name, obj.partner.first_name, obj.partner.patronymic])

    def get_idea(self, obj):
        return obj.idea.caption


class DetailTeamSerializer(serializers.ModelSerializer):
    """Сериализатор команды для создания/обновления"""


    class Meta:
        model = Team
        fields = [
            'id',
            'caption',
            'leader',
            'expert',
            'partner',
            'idea',
        ]



class TeamViewSet(viewsets.ModelViewSet):
    """Представление команды"""
    permission_classes = [permissions.AllowAny]

    queryset = Team.objects.all()
    available_serializers = {
        'list': TeamSerializer,
        'destroy': TeamSerializer,

        'retrieve': DetailTeamSerializer,
        'partial_update': DetailTeamSerializer,
        'create': DetailTeamSerializer,
    }

    def get_serializer_class(self):
        """выбор сериализатора"""
        if self.action not in self.available_serializers:
            raise RuntimeError(f'Action {self.action} does not supported')
        serializer_class = self.available_serializers[self.action]
        return serializer_class
