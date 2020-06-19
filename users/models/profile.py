from django.contrib.auth.models import AbstractUser
from django.db import models

from organization.models import Department
from . import Position


class Profile(AbstractUser):
    """Профиль пользователя."""
    username = None
    email = models.EmailField(
        verbose_name='Емайл',
        unique=True
    )
    patronymic = models.CharField(
        max_length=128,
        verbose_name='Отчество',
    )
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Департамент',
    )
    position = models.ForeignKey(
        Position,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Должность',
    )
    photo = models.FileField(
        verbose_name='Аватар',
        null=True,
        blank=True,
        upload_to='avatars/',
    )
    phone = models.CharField(
        max_length=32,
        verbose_name='Телефон',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['department', 'position']

    def __str__(self):
        return self.email
