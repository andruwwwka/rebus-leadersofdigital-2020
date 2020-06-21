from django.db import models

from .history import History


class BaseAchievement(models.Model):
    """Базовый класс для бейджей/наград."""
    name = models.CharField(
        max_length=128,
        verbose_name='Наименование бейджа/награды',
    )
    uid = models.SlugField(
        verbose_name='Идентификатор',
    )
    cost = models.IntegerField(
        verbose_name='Стоимость',
    )
    archive = models.NullBooleanField(
        default=False,
        verbose_name='Архивный'
    )

    target_attribute = None

    class Meta:
        abstract = True

    def assign_to_user(self, profile):
        """Присвоение пользователю достижения."""
        if not self.target_attribute:
            raise AttributeError('Неверная операция. Целевой атрибут не присвоен.')
        trans_data = {
            self.target_attribute: self,
            'amount': self.cost,
            'profile': profile
        }
        transaction = History(**trans_data)
        return transaction

    def __str__(self):
        return self.name
