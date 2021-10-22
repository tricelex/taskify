from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseAbstractModel(models.Model):
    created_datetime = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_datetime = models.DateTimeField(_('Last Update at'), auto_now=True)

    class Meta:
        abstract = True
