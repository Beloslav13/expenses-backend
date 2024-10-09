from django.core.exceptions import ValidationError
from django.db import models

from expenses.models.base import BaseModel
from expenses.models.category import Category
from expenses.models.user import User


class Spending(BaseModel):
    user: User = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='spendings'
    )
    category: Category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='spendings'
    )
    name = models.CharField("Название", max_length=100)
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def clean(self):
        if self.category.user != self.user:
            raise ValidationError('Category does not belong to the user')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
