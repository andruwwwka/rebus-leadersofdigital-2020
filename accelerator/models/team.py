from django.db import models

from accelerator.models import Tender
from users.models import Profile


class Team(models.Model):
    """Команда, которая отвечает за реализацию идеи."""
    caption = models.CharField(
        verbose_name='Наименование команды',
        max_length=128,
    )
    leader = models.ForeignKey(
        Profile,
        null=True,
        related_name='leader_teams',
        on_delete=models.SET_NULL,
        verbose_name='Капитан',
    )
    expert = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Куратор',
    )
    partner = models.ManyToManyField(
        Profile,
        related_name='teams',
        verbose_name='Участник команды',
    )
    idea = models.ForeignKey(
        Tender,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Идея/Предложение',
    )

    def __str__(self):
        return '{0}: {1}'.format(self.caption, self.idea.caption)
