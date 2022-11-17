from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=65, null=True, blank=True)
    task_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
   
