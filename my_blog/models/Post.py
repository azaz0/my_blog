from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Tytuł')
    content = models.TextField(verbose_name='Treść')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Data publikacji')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    categories = models.ManyToManyField('Category', related_name='posts', blank=True, verbose_name='Kategorie')
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True, verbose_name='Tagi')
    slug = models.SlugField(unique=True, max_length=255, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posty'
        ordering = ['-date_posted']
