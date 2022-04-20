from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class TodoContent(models.Model):
    todo_text = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todolist',  null=True)

    def __str__(self):
        return self.todo_text
