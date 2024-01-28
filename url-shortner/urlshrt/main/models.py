from django.db import models

class Links(models.Model):
    url = models.TextField('Ссылка')
    alias = models.CharField('Алиас', max_length=12)
    date = models.DateTimeField('Дата добавления')

    # def __str__(self):
    #     return self.url, self.alias      #НЕПОНЯТНО

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
