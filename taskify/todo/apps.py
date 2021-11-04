from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TodoConfig(AppConfig):
    name = "taskify.todo"
    verbose_name = _("Todos")
