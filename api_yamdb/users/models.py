from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import username_validator

ROLES = (('admin', 'admin'),
         ('moderator', 'moderator'),
         ('user', 'user'))


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Имя пользователя',
        validators=[username_validator()])
    email = models.EmailField(
        max_length=254,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Email')
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Имя')
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Фамилия')
    bio = models.TextField(
        verbose_name='О себе',
        blank=True,
        null=True)
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='user')
    confirmation_code = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Код проверки')

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ['username']

    def __str__(self) -> str:
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_user(self):
        return self.role == 'user'
