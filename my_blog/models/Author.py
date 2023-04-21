from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Użytkownik')
    bio = models.TextField(verbose_name='Opis')
    website = models.URLField(verbose_name='Strona internetowa', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'
