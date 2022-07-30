from django.db import models


class Todo(models.Model):
    title = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'