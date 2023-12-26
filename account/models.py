from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=250, verbose_name='full name')

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name_plural = 'account users'
        ordering = ['-id']




