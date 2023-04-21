from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name='Adres email')
    is_active = models.BooleanField(default=True, verbose_name='Aktywny')
    date_subscribed = models.DateTimeField(auto_now_add=True, verbose_name='Data subskrypcji')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subskrybent'
        verbose_name_plural = 'Subskrybenci'
