from django.db import models

# Create your models here.
# Everytime you make a change to a database model you need to make a migration

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)