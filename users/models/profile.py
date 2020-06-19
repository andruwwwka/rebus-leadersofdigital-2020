from django.contrib.auth.models import AbstractUser
from django.db import models

from . import Position
from ..organization.models import Department


class Profile(AbstractUser):
    """Профиль пользователя."""
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL
    )
