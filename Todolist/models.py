from django.db import models

# Create your models here.

class Todolist(models.Model):
    subject=models.CharField(max_length=20)
    content=models.CharField(max_length=500)

