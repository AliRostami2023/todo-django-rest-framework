from django.db import models
from account.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todo')
    title = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'todos'

