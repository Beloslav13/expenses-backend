from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, username, email, external_id, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, external_id=external_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, external_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, external_id, password, **extra_fields)


class User(AbstractUser):
    external_id = models.IntegerField("Внешний id", unique=True, blank=True, null=True, db_index=True)
    is_bot = models.BooleanField("Бот", default=False)
    is_premium = models.BooleanField("Премиум аккаунт", default=False)

    objects = UserManager()

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['email', 'external_id']
