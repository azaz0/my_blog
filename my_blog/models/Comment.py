from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', verbose_name='Post')
    content = models.TextField(verbose_name='Treść')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Data dodania')

    def __str__(self):
        return f'Komentarz dodany przez {self.author} dla posta {self.post}'

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'
        ordering = ['-date_posted']
