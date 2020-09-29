from django.db import models

class Todo(models.Model):
    added_date = models.DateTimeField()
    entry_text = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.added_date} -> {self.entry_text}"   
