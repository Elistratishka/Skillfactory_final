from django.db import models
from django.contrib.auth.models import User


class LoginCode(models.Model):
    code = models.IntegerField('код авторизации')
    user = models.OneToOneField(User, verbose_name='пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Код авторизации'
        verbose_name_plural = 'Коды авторизации'
