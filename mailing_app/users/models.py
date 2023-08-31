from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватар')
    conformation_code = models.CharField(max_length=10, **NULLABLE, verbose_name='Ключ верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []