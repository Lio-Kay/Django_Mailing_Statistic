from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Permission

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Кастомная модель пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(**NULLABLE, max_length=50, verbose_name='Имя')
    last_name = models.CharField(**NULLABLE, max_length=50, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватар')
    conformation_code = models.CharField(max_length=10, **NULLABLE, verbose_name='Ключ верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
