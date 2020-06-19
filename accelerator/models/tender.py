from django.db import models

from accelerator.models.reference import TENDER_STATUSES, TENDER_TYPES, TENDER_DIRECTIONS
from organization.models import Department
from users.models import Profile


class Tender(models.Model):
    """Идея/предложение, вынесенное на обсуждение."""
    caption = models.CharField(
        max_length=128,
        verbose_name='Наименование',
    )
    description = models.TextField(
        max_length=4000,
        verbose_name='Описание',
    )
    direction = models.CharField(
        max_length=16,
        choices=TENDER_DIRECTIONS,
        default='technology',
        verbose_name='Направление/Категория',
    )
    presentation = models.FileField(
        verbose_name='Файлы презентации',
        null=True,
        blank=True,
        upload_to='files/',
    )
    status = models.CharField(
        max_length=16,
        choices=TENDER_STATUSES,
        verbose_name='Статус',
        default='draft',
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор идеи/предложения',
    )
    tender_type = models.CharField(
        verbose_name='Тип идеи/предложения',
        max_length=16,
        choices=TENDER_TYPES,
        default='idea',
    )
    area = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Зона видимости',
    )

    def __str__(self):
        return '{0} {1}: {2}'.format(self.owner.last_name, self.owner.first_name, self.caption)
