from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    update = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title