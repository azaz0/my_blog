from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories',
                                   verbose_name='Utworzona przez')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'
        ordering = ['name']
