from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        abstract = True
        ordering = ['id']

    @property
    def entity_name(self):
        return f'{self.__class__.__name__}#{self.pk}'

    @property
    def entity_model(self):
        return f'{self.__class__.__name__}'.lower()

    def __str__(self):
        return self.entity_name
