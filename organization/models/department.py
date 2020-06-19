from django.db import models


class Department(models.Model):
    """Структура организации."""
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
    )
    name = models.CharField(
        verbose_name='Наименование подразделения',
        max_length=256,
    )

    def __str__(self):
        return self.name

