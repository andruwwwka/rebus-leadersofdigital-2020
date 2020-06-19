from django.db import models


class Department(models.Model):
    """Структура организации."""
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
