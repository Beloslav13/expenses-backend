from django.db import models
from django.db.models.functions import Lower

from expenses.models.base import BaseModel
from expenses.models.user import User


class Category(BaseModel):
    user: User = models.ForeignKey(to=User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='categories')
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

        constraints = [
            models.UniqueConstraint(Lower('name'), 'user', name="unique_category"),
        ]

    def __str__(self):
        return f'{self.name} - {self.user.username}'
