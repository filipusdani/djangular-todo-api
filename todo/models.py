from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(default=0)
    order = models.IntegerField(default=1)
 
    def __str__(self) -> str:
        return self.task
    
class TodoCategory(models.Model):
    tag = models.CharField(max_length=3)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.tag