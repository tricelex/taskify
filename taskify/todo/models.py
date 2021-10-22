from django.db import models

from taskify.utils.models import BaseAbstractModel


class List(BaseAbstractModel):
    title = models.CharField(max_length=250)


class Task(BaseAbstractModel):
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
