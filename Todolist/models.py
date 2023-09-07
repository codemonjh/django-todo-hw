from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todolist(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=20)
    content=models.CharField(max_length=500)
    is_complete=models.BooleanField(default=False)

