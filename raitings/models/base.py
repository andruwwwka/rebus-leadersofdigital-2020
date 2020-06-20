from django.db import models

from .history.models import History


class BaseAchievement(models.Model):
    """Базовый класс для ачивок."""
    name = models.CharField()
    uid = models.SlugField()
    cost = models.IntegerField()
    archive = models.BooleanField()

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
