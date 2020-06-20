from django.db import models


class History(models.Model):
    """Модель истории назначения наград/бейджей"""
    amount = models.IntegerField(
        verbose_name='Количество',
    )
    badge = models.ForeignKey(
        'Badge',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Бейдж',
    )
    reward = models.ForeignKey(
        'Reward',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Награда',
    )
    profile = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        verbose_name='Владелец',
    )
    receiving_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата награждения',
    )

    def __str__(self):
        return '{0} {1}'.format(
            self.reward.name or self.badge.name or '',
            self.receiving_date.strftime('%d.%m.%Y'),
        )
