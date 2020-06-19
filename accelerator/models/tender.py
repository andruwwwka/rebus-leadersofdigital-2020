from django.db import models


class Tender(models.Model):
    """Идея/предложение, вынесенное на обсуждение."""
    caption = models.CharField(
        max_length=128,
        verbose_name='Наименование',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    direction = models.CharField(
        max_length=16,
        choices=[],
        verbose_name='Направление/Категория',
    )
    presentation = models.FileField(
        verbose_name='Файлы презентации',
    )
    status = models.CharField(
        max_length=16,
        choices=[],
        verbose_name='Статус',
        default='draft',
    )
    owner = models.ForeignKey(
        on_delete=SET_NULL,

    )
