from django.db import models
from django.db.models import TextChoices


# Create your models here.


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активно'
    BLOCKED = 'BLOCKED', 'Заблокировано'


class GuestBook(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Имя гостя')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='e-mail')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Имя гостя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Статус',
        default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return f"{self.name} {self.email} {self.text} {self.status}"
