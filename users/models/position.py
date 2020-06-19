from django.db import models


class Position(models.Model):
    """Должности сотрудников."""
    post = models.CharField(
        max_length=256,
    )

    def __str__(self):
        return self.post
