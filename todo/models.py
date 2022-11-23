from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserTodo(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, primary_key=True)
    todos = models.TextField()

    def __str__(self):
        return self.owner.username
