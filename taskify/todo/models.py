import uuid

from django.db import models
from django.urls import reverse

from taskify.utils.models import BaseAbstractModel


class TaskList(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todos:task_list_detail', kwargs={'uuid': self.id})


class Task(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
