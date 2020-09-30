from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} -> {self.time_added}'