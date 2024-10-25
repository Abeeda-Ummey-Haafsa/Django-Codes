from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    category = models.ManyToManyField(Category) 
    taskAssignDate = models.DateField()
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle