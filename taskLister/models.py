from django.db import models
from django.urls import reverse


# Create your models here.
class Tasks(models.Model):
    task_title=models.CharField(max_length=50)
    def __str__(self):
        return self.task_title
    
    def get_absolute_url(self):
        return reverse('taskLister:tasks-list', args=[self.id])
    
