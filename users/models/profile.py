from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from organization.models import Department
from . import Position


class ProfileManager(BaseUserManager):
    """Менеджер для создания пользователей."""

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Данный адрес электронной почты должен быть установлен')
        email = self.normalize_email(email)
        department = extra_fields.get('department')
        if isinstance(department, int) or isinstance(department, str) and department.isdigit():
            extra_fields['department'] = Department.objects.get(id=department)
        position = extra_fields.get('position')
        if isinstance(position, int) or isinstance(position, str) and position.isdigit():
            extra_fields['position'] = Position.objects.get(id=department)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает `User` с адресом электронной почты, именем пользователя и паролем."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Создает и возвращает пользователя с правами суперпользователя (администратора)."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    """Профиль пользователя."""
    username = None
    email = models.EmailField(
        verbose_name='Емайл',
        unique=True
    )
    patronymic = models.CharField(
        max_length=128,
        blank=True,
        null=True,
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
        blank=True,
        verbose_name='Телефон',
    )
    internal_phone = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='Внутренний телефон',
    )
    city = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Город',
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['department', 'position']

    objects = ProfileManager()

    def __str__(self):
        return self.email
