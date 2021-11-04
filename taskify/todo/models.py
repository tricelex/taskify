import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

from taskify.utils.models import BaseAbstractModel


class TaskList(BaseAbstractModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=125, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="user",
    )

    def __str__(self):
        return f"{self.title} - {self.user}"

    def get_absolute_url(self):
        return reverse("todos:task_list_detail", kwargs={"uuid": self.id})


class Task(BaseAbstractModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
