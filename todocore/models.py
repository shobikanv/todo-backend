from django.db import models


class Task(models.Model):
    task_title = models.CharField(max_length=400, blank=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
