from django.db import models

from accelerator.models import Team, Tender


class Round(models.Model):
    """Раунд акселерации."""
    # название
    # дата начала
    # дата завершения
    # команда или идея? наверное команда, так как там есть связь с идеей

    caption = models.CharField(
        verbose_name='Наименование раунда',
        max_length=128,
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата старта раунда',
    )
    finish_date = models.DateTimeField(
        verbose_name='Дата завершения раунда',
    )
    tender = models.ForeignKey(
        Tender,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Идея/Предложение',
    )

    def __str__(self):
        return '{0}: {1}/{2}'.format(
            self.tender.caption,
            self.start_date.strftime('%d.%m.%Y'),
            self.finish_date.strftime('%d.%m.%Y'),
        )
