from django.db import models

# Create your models here.


class Todo(models.model):
    title = models.CharField(max_length= 200)
