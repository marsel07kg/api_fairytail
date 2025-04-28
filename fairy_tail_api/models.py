from django.db import models

class Character(models.Model):
    name = models.TextField(verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='fairy_tail/%y/%m/%d/',)

    class Meta:
        verbose_name = 'персонажи хвост феи'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
# Create your models here.
