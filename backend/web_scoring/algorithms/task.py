import time
from .algorithm import algorithm_process
from .models import Task


def create_process_task(task_id, path):
    instance = Task.objects.get(id=task_id)
    algorithm_process(path)
    instance.status = True
    instance.save()
