from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskName = models.CharField(max_length=150)


    def __str__(self):
        return self.taskName