from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    file_path = models.FilePathField(path="/media/", default="/media/null.json", recursive=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
